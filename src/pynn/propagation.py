import logging
import math

import pynn.activation as act


class Propagation:
    def __init__(self, nn):
        self.n = nn
        self._neuron = nn.neuron
        self._weight = nn.transfer_weight
        self._input = nn.transfer_input
        self._target = nn.transfer_target
        self._activation_mode = nn.activation_mode
        self._loss_mode = nn.loss_mode

    def calc_neurons(self) -> None:
        """
        Calculating neurons.
        """
        length, dec = self.n.len_input, 0
        for i in range(len(self._neuron)):
            if i > 0:
                dec = i - 1
                length = len(self._neuron[dec])

            for j in range(len(self._neuron[i])):
                self._neuron[i][j].value = num = 0.
                for k in range(len(self._weight[i][j])):
                    if k < length:
                        if i > 0:
                            self._neuron[i][j].value += self._neuron[dec][k].value * self._weight[i][j][k]
                        else:
                            self._neuron[i][j].value += self._input[k] * self._weight[i][j][k]
                    else:
                        self._neuron[i][j].value += self._weight[i][j][k]
                    num += 1

                if self._activation_mode == self.n.LINEAR:
                    if num != 0:
                        self._neuron[i][j].value /= num
                else:
                    self._neuron[i][j].value = act.activation(self._neuron[i][j].value, self._activation_mode)

    def calc_loss(self) -> float:
        """
        Calculating and return the error of the output neurons.
        """
        # TODO: try-catch
        loss = 0.
        for i in range(len(self._neuron[self.n.last_layer_ind])):
            self._neuron[self.n.last_layer_ind][i].miss = self._target[i] - self._neuron[self.n.last_layer_ind][i].value
            match self._loss_mode:
                case self.n.MSE, self.n.RMSE, _:
                    loss += self._neuron[self.n.last_layer_ind][i].miss ** 2
                case self.n.ARCTAN:
                    loss += math.atan(self._neuron[self.n.last_layer_ind][i].miss) ** 2
                case self.n.AVG:
                    loss += math.fabs(self._neuron[self.n.last_layer_ind][i].miss)

        loss /= self.n.len_output
        if self._loss_mode == self.n.RMSE:
            loss = math.sqrt(loss)

        match True:
            case math.isnan(loss):
                logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
            case math.isinf(loss):
                logging.log(0, 'perceptron.calc_loss: loss is infinity')
        return loss

    def calc_miss(self) -> None:
        """
        Calculating the error of neuron in hidden layers.
        """
        if self.n.last_layer_ind > 0:
            for i in range(self.n.last_layer_ind - 1, -1, -1):
                inc = i + 1
                for j in range(len(self._neuron[i])):
                    self._neuron[i][j].miss = 0.
                    for k, m in range(len(self._neuron[inc])):
                        self._neuron[i][j].miss += self._neuron[inc][k].miss * self._weight[inc][k][j]

    def update_weights(self) -> None:
        """
        Update weights.
        """
        length, dec = self.n.len_input, 0
        for i in range(len(self._weight)):
            if i > 0:
                dec = i - 1
                length = len(self._neuron[dec])

            for j in range(len(self._weight[i])):
                grad = self.n.rate * self._neuron[i][j].miss * act.derivative(self._neuron[i][j].value,
                                                                              self._activation_mode)
                for k in range(len(self._weight[i][j])):
                    if k < length:
                        val: float
                        if i > 0:
                            val = self._neuron[dec][k].value
                        else:
                            val = self._input[k]

                        if self._activation_mode == self.n.LINEAR:
                            if val != 0:
                                self._weight[i][j][k] += grad / val
                        else:
                            self._weight[i][j][k] += grad * val
                    else:
                        self._weight[i][j][k] += grad


"""
// calcNeuron.
func (nn *NN) calcNeuron() {
	var length, dec int
	for i, v := range nn.neuron {
		if i > 0 {
			dec = i - 1
			length = len(nn.neuron[dec])
		} else {
			length = nn.lenInput
		}

		for j, n := range v {
			var num pkg.FloatType = 0
			n.value = 0
			for k, w := range nn.weights[i][j] {
				if k < length {
					if i > 0 {
						n.value += nn.neuron[dec][k].value * w
					} else {
						n.value += nn.input[k] * w
					}
				} else {
					n.value += w
				}
				num++
			}

			switch nn.ActivationMode {
			case params.LINEAR:
				if num > 0 {
					n.value /= num
				}
			default:
				n.value = params.Activation(n.value, nn.ActivationMode)
			}
		}
	}
}

// calcLoss calculating the error of the output neuron.
func (nn *NN) calcLoss() (loss float64) {
	for i, n := range nn.neuron[nn.lastLayerIndex] {
		n.miss = nn.target[i] - n.value
		switch nn.LossMode {
		default:
			fallthrough
		case params.MSE, params.RMSE:
			loss += math.Pow(float64(n.miss), 2)
		case params.ARCTAN:
			loss += math.Pow(math.Atan(float64(n.miss)), 2)
		case params.AVG:
			loss += math.Abs(float64(n.miss))
		}
	}

	loss /= float64(nn.lenOutput)
	if nn.LossMode == params.RMSE {
		loss = math.Sqrt(loss)
	}

	switch {
	case math.IsNaN(loss):
		log.Panic("perceptron.NN.calcLoss: loss not-a-number value") // TODO: log.Panic (?)
	case math.IsInf(loss, 0):
		log.Panic("perceptron.NN.calcLoss: loss is infinity") // TODO: log.Panic (?)
	}
	return
}

// calcMiss calculating the error of neuron in hidden layers.
func (nn *NN) calcMiss() {
	if nn.lastLayerIndex > 0 {
		for i := nn.lastLayerIndex - 1; i >= 0; i-- {
			inc := i + 1
			for j, n := range nn.neuron[i] {
				n.miss = 0
				for k, m := range nn.neuron[inc] {
					n.miss += m.miss * nn.weights[inc][k][j]
				}
			}
		}
	}
}

// updateWeight update weights.
func (nn *NN) updateWeight() {
	var length, dec int
	for i, v := range nn.weights {
		if i > 0 {
			dec = i - 1
			length = len(nn.neuron[dec])
		} else {
			length = nn.lenInput
		}

		for j, w := range v {
			grad := nn.Rate * nn.neuron[i][j].miss * params.Derivative(nn.neuron[i][j].value, nn.ActivationMode)
			for k := range w {
				if k < length {
					var value pkg.FloatType
					if i > 0 {
						value = nn.neuron[dec][k].value
					} else {
						value = nn.input[k]
					}

					switch nn.ActivationMode {
					case params.LINEAR:
						if value != 0 {
							nn.weights[i][j][k] += grad / value
						}
					default:
						nn.weights[i][j][k] += grad * value
					}
				} else {
					nn.weights[i][j][k] += grad
				}
			}
		}
	}
}
"""
