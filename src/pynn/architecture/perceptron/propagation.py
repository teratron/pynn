import logging
import math
from typing import Union

from pynn.utils import loss, activation


# from .parameters import Parameters
# from .properties import Properties


class Propagation:  # (Parameters, Properties)
    """
    Propagation.
    """

    # def __init__(self):
    #     pass

    def calc_neurons(self: Union[object, None]) -> None:
        """
        Calculating neurons.
        """
        length, dec = self.len_input, 0
        for i in range(len(self.neurons)):
            if i > 0:
                dec = i - 1
                length = len(self.neurons[dec])

            for j in range(len(self.neurons[i])):
                self.neurons[i][j].value = num = 0.
                for k in range(len(self.data_weight[i][j])):
                    if k < length:
                        if i > 0:
                            self.neurons[i][j].value += self.neurons[dec][k].value * self.data_weight[i][j][k]
                        else:
                            self.neurons[i][j].value += self.data_input[k] * self.data_weight[i][j][k]
                    else:
                        self.neurons[i][j].value += self.data_weight[i][j][k]
                    num += 1

                if self.activation_mode == activation.Mode.LINEAR:
                    if num > 0:
                        self.neurons[i][j].value /= num
                else:
                    self.neurons[i][j].value = activation.activation(self.neurons[i][j].value, self.activation_mode)

    def calc_loss(self) -> float:
        """
        Calculating and return the total error of the output neurons.
        """
        # TODO: try-catch
        error = 0.
        for i in range(self.len_output):
            self.neurons[self.last_layer_ind][i].miss = self.data_target[i] - self.neurons[self.last_layer_ind][i].value
            match self.loss_mode:
                case loss.Mode.MSE, loss.Mode.RMSE, _:
                    error += self.neurons[self.last_layer_ind][i].miss ** 2
                case loss.Mode.ARCTAN:
                    error += math.atan(self.neurons[self.last_layer_ind][i].miss) ** 2
                case loss.Mode.AVG:
                    error += math.fabs(self.neurons[self.last_layer_ind][i].miss)

        error /= self.len_output
        if self.loss_mode == loss.Mode.RMSE:
            error = math.sqrt(error)

        match True:
            case math.isnan(error):
                logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
            case math.isinf(error):
                logging.log(0, 'perceptron.calc_loss: loss is infinity')

        return error

    def calc_miss(self) -> None:
        """
        Calculating the error of neuron in hidden layers.
        """
        if self.last_layer_ind > 0:
            for i in range(self.last_layer_ind - 1, -1, -1):
                inc = i + 1
                for j in range(len(self.neurons[i])):
                    self.neurons[i][j].miss = 0.
                    for k, m in range(len(self.neurons[inc])):
                        self.neurons[i][j].miss += self.neurons[inc][k].miss * self.data_weight[inc][k][j]

    def update_weights(self) -> None:
        """
        Update weights.
        """
        length, dec = self.len_input, 0
        for i in range(len(self.data_weight)):
            if i > 0:
                dec = i - 1
                length = len(self.neurons[dec])

            for j in range(len(self.data_weight[i])):
                grad = self.rate * self.neurons[i][j].miss * activation.derivative(self.neurons[i][j].value,
                                                                                   self.activation_mode)
                for k in range(len(self.data_weight[i][j])):
                    if k < length:
                        val: float
                        if i > 0:
                            val = self.neurons[dec][k].value
                        else:
                            val = self.data_input[k]

                        if self.activation_mode == activation.Mode.LINEAR:
                            if val != 0:
                                self.data_weight[i][j][k] += grad / val
                        else:
                            self.data_weight[i][j][k] += grad * val
                    else:
                        self.data_weight[i][j][k] += grad


# def calc_neurons(obj) -> None:
#     length, dec = obj.len_input, 0
#     for i in range(len(obj.neurons)):
#         if i > 0:
#             dec = i - 1
#             length = len(obj.neurons[dec])
# 
#         for j in range(len(obj.neurons[i])):
#             obj.neurons[i][j].value = num = 0.
#             for k in range(len(obj.data_weight[i][j])):
#                 if k < length:
#                     if i > 0:
#                         obj.neurons[i][j].value += obj.neurons[dec][k].value * obj.data_weight[i][j][k]
#                     else:
#                         obj.neurons[i][j].value += obj.data_input[k] * obj.data_weight[i][j][k]
#                 else:
#                     obj.neurons[i][j].value += obj.data_weight[i][j][k]
#                 num += 1
# 
#             if obj.activation_mode == obj.LINEAR:
#                 if num > 0:
#                     obj.neurons[i][j].value /= num
#             else:
#                 obj.neurons[i][j].value = act.activation(obj.neurons[i][j].value, obj.activation_mode)


# def calc_loss(obj) -> float:
#     # TODO: try-catch
#     loss = 0.
#     for i in range(obj.len_output):
#         obj.neurons[obj.last_layer_ind][i].miss = obj.data_target[i] - obj.neurons[obj.last_layer_ind][i].value
#         match obj.loss_mode:
#             case obj.MSE, obj.RMSE, _:
#                 loss += obj.neurons[obj.last_layer_ind][i].miss ** 2
#             case obj.ARCTAN:
#                 loss += math.atan(obj.neurons[obj.last_layer_ind][i].miss) ** 2
#             case obj.AVG:
#                 loss += math.fabs(obj.neurons[obj.last_layer_ind][i].miss)
# 
#     loss /= obj.len_output
#     if obj.loss_mode == obj.RMSE:
#         loss = math.sqrt(loss)
# 
#     match True:
#         case math.isnan(loss):
#             logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
#         case math.isinf(loss):
#             logging.log(0, 'perceptron.calc_loss: loss is infinity')
# 
#     return loss


# def calc_miss(obj) -> None:
#     if obj.last_layer_ind > 0:
#         for i in range(obj.last_layer_ind - 1, -1, -1):
#             inc = i + 1
#             for j in range(len(obj.neurons[i])):
#                 obj.neurons[i][j].miss = 0.
#                 for k, m in range(len(obj.neurons[inc])):
#                     obj.neurons[i][j].miss += obj.neurons[inc][k].miss * obj.data_weight[inc][k][j]


# def update_weights(obj) -> None:
#     """
#     Update weights.
#     """
#     length, dec = obj.len_input, 0
#     for i in range(len(obj.data_weight)):
#         if i > 0:
#             dec = i - 1
#             length = len(obj.neurons[dec])
# 
#         for j in range(len(obj.data_weight[i])):
#             grad = obj.rate * obj.neurons[i][j].miss * act.derivative(obj.neurons[i][j].value, obj.activation_mode)
#             for k in range(len(obj.data_weight[i][j])):
#                 if k < length:
#                     val: float
#                     if i > 0:
#                         val = obj.neurons[dec][k].value
#                     else:
#                         val = obj.data_input[k]
# 
#                     if obj.activation_mode == obj.LINEAR:
#                         if val != 0:
#                             obj.data_weight[i][j][k] += grad / val
#                     else:
#                         obj.data_weight[i][j][k] += grad * val
#                 else:
#                     obj.data_weight[i][j][k] += grad


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
