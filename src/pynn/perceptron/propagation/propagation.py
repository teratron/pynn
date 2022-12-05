from .calc_loss import calc_loss
from .calc_miss import calc_miss
from .calc_neurons import calc_neurons
from .update_weights import update_weights


class Propagation:
    """
    Propagation.
    """

    # def __init__(self, nn):
    #     self.n = nn

    def calc_neurons(self) -> None:
        """
        Calculating neurons.
        """
        calc_neurons(self)

        # length, dec = self.n.len_input, 0
        # for i in range(len(self.n.neuron)):
        #     if i > 0:
        #         dec = i - 1
        #         length = len(self.n.neuron[dec])
        #
        #     for j in range(len(self.n.neuron[i])):
        #         self.n.neuron[i][j].value = num = 0.
        #         for k in range(len(self.n.data_weight[i][j])):
        #             if k < length:
        #                 if i > 0:
        #                     self.n.neuron[i][j].value += self.n.neuron[dec][k].value * self.n.data_weight[i][j][k]
        #                 else:
        #                     self.n.neuron[i][j].value += self.n.data_input[k] * self.n.data_weight[i][j][k]
        #             else:
        #                 self.n.neuron[i][j].value += self.n.data_weight[i][j][k]
        #             num += 1
        #
        #         if self.n.activation_mode == self.n.LINEAR:
        #             if num > 0:
        #                 self.n.neuron[i][j].value /= num
        #         else:
        #             self.n.neuron[i][j].value = act.activation(self.n.neuron[i][j].value, self.n.activation_mode)

    def calc_loss(self) -> float:
        """
        Calculating and return the total error of the output neurons.
        """
        return calc_loss(self)

        # TODO: try-catch
        # loss = 0.
        # for i in range(self.n.len_output):
        #     self.n.neuron[self.n.last_layer_ind][i].miss = self.n.data_target[i] - \
        #                                                    self.n.neuron[self.n.last_layer_ind][i].value
        #     match self.n.loss_mode:
        #         case self.n.MSE, self.n.RMSE, _:
        #             loss += self.n.neuron[self.n.last_layer_ind][i].miss ** 2
        #         case self.n.ARCTAN:
        #             loss += math.atan(self.n.neuron[self.n.last_layer_ind][i].miss) ** 2
        #         case self.n.AVG:
        #             loss += math.fabs(self.n.neuron[self.n.last_layer_ind][i].miss)
        #
        # loss /= self.n.len_output
        # if self.n.loss_mode == self.n.RMSE:
        #     loss = math.sqrt(loss)
        #
        # match True:
        #     case math.isnan(loss):
        #         logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
        #     case math.isinf(loss):
        #         logging.log(0, 'perceptron.calc_loss: loss is infinity')
        # return loss

    def calc_miss(self) -> None:
        """
        Calculating the error of neuron in hidden layers.
        """
        calc_miss(self)

        # if self.n.last_layer_ind > 0:
        #     for i in range(self.n.last_layer_ind - 1, -1, -1):
        #         inc = i + 1
        #         for j in range(len(self.n.neuron[i])):
        #             self.n.neuron[i][j].miss = 0.
        #             for k, m in range(len(self.n.neuron[inc])):
        #                 self.n.neuron[i][j].miss += self.n.neuron[inc][k].miss * self.n.data_weight[inc][k][j]

    def update_weights(self) -> None:
        """
        Update weights.
        """
        update_weights(self)

        # length, dec = self.n.len_input, 0
        # for i in range(len(self.n.data_weight)):
        #     if i > 0:
        #         dec = i - 1
        #         length = len(self.n.neuron[dec])
        #
        #     for j in range(len(self.n.data_weight[i])):
        #         grad = self.n.rate * self.n.neuron[i][j].miss * act.derivative(self.n.neuron[i][j].value,
        #                                                                        self.n.activation_mode)
        #         for k in range(len(self.n.data_weight[i][j])):
        #             if k < length:
        #                 val: float
        #                 if i > 0:
        #                     val = self.n.neuron[dec][k].value
        #                 else:
        #                     val = self.n.data_input[k]
        #
        #                 if self.n.activation_mode == self.n.LINEAR:
        #                     if val != 0:
        #                         self.n.data_weight[i][j][k] += grad / val
        #                 else:
        #                     self.n.data_weight[i][j][k] += grad * val
        #             else:
        #                 self.n.data_weight[i][j][k] += grad


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
