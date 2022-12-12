from pynn.architecture.perceptron.propagation.calc_loss import calc_loss
from pynn.architecture.perceptron.propagation.calc_miss import calc_miss
from pynn.architecture.perceptron.propagation.calc_neurons import calc_neurons
from pynn.architecture.perceptron.propagation.update_weights import update_weights


class Propagation:
    """
    Propagation.
    """

    def calc_neurons(self) -> None:
        """Calculating neurons."""
        calc_neurons(self)

    def calc_loss(self) -> float:
        """Calculating and return the total error of the output neurons."""
        return calc_loss(self)

    def calc_miss(self) -> None:
        """Calculating the error of neuron in hidden layers."""
        calc_miss(self)

    def update_weights(self) -> None:
        """Update weights."""
        update_weights(self)


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
