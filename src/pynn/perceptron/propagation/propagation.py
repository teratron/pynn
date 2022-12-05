from .calc_loss import calc_loss
from .calc_miss import calc_miss
from .calc_neurons import calc_neurons
from .update_weights import update_weights


class Propagation:
    """
    Propagation.
    """

    def calc_neurons(self) -> None:
        """
        Calculating neurons.
        """
        calc_neurons(self)

    def calc_loss(self) -> float:
        """
        Calculating and return the total error of the output neurons.
        """
        return calc_loss(self)

    def calc_miss(self) -> None:
        """
        Calculating the error of neuron in hidden layers.
        """
        calc_miss(self)

    def update_weights(self) -> None:
        """
        Update weights.
        """
        update_weights(self)


"""
// Init initialize.
func (nn *NN) Init(data ...interface{}) {
	var err error
	if len(data) > 0 {
		switch value := data[0].(type) {
		case utils.Filer:
			if _, ok := value.(utils.FileError); !ok {
				if len(nn.Weights) > 0 {
					nn.initFromWeight()
				}
				nn.config = value
			}
		case int:
			if len(data) == 2 {
				if v, ok := data[1].(int); ok {
					nn.initFromNew(value, v)
				}
			}
		default:
			err = fmt.Errorf("%T %w: %v", value, pkg.ErrMissingType, value)
		}
		if err == nil {
			nn.initCompletion()
		}
	} else {
		err = pkg.ErrNoArgs
	}

	if err != nil {
		log.Printf("perceptron.NN.Init: %v\n", err)
	}
}

// initFromNew initialize.
func (nn *NN) initFromNew(lenInput, lenTarget int) {
	nn.lenInput = lenInput
	nn.lenOutput = lenTarget
	nn.lastLayerIndex = len(nn.HiddenLayer)
	if nn.lastLayerIndex > 0 && nn.HiddenLayer[0] == 0 {
		nn.lastLayerIndex = 0
	}

	var layer []uint
	if nn.lastLayerIndex > 0 {
		layer = append(nn.HiddenLayer, uint(nn.lenOutput))
	} else {
		layer = []uint{uint(nn.lenOutput)}
	}
	lenLayer := len(layer)

	bias := 0
	if nn.Bias {
		bias = 1
	}
	biasInput := nn.lenInput + bias
	var biasLayer int

	nn.Weights = make(pkg.Float3Type, lenLayer)
	nn.weights = make(pkg.Float3Type, lenLayer)
	nn.neuron = make([][]*neuron, lenLayer)
	for i, v := range layer {
		nn.Weights[i] = make(pkg.Float2Type, v)
		nn.weights[i] = make(pkg.Float2Type, v)
		nn.neuron[i] = make([]*neuron, v)
		if i > 0 {
			biasLayer = int(layer[i-1]) + bias
		}

		for j := 0; j < int(v); j++ {
			if i > 0 {
				nn.Weights[i][j] = make(pkg.Float1Type, biasLayer)
				nn.weights[i][j] = make(pkg.Float1Type, biasLayer)
			} else {
				nn.Weights[i][j] = make(pkg.Float1Type, biasInput)
				nn.weights[i][j] = make(pkg.Float1Type, biasInput)
			}
			for k := range nn.weights[i][j] {
				if nn.ActivationMode == params.LINEAR {
					nn.Weights[i][j][k] = .5
				} else {
					nn.Weights[i][j][k] = params.GetRandFloat()
				}
			}
			nn.neuron[i][j] = &neuron{}
		}
	}
}

// initFromWeight.
func (nn *NN) initFromWeight() {
	length := len(nn.Weights)

	if !nn.Bias && length > 1 && len(nn.Weights[0])+1 == len(nn.Weights[1][0]) {
		nn.Bias = true
	}

	nn.lastLayerIndex = length - 1
	nn.lenOutput = len(nn.Weights[nn.lastLayerIndex])
	nn.lenInput = len(nn.Weights[0][0])
	if nn.Bias {
		nn.lenInput -= 1
	}

	if nn.lastLayerIndex > 0 {
		nn.HiddenLayer = make([]uint, nn.lastLayerIndex)
		for i := range nn.HiddenLayer {
			nn.HiddenLayer[i] = uint(len(nn.Weights[i]))
		}
	} else {
		nn.HiddenLayer = []uint{0}
	}

	nn.weights = make(pkg.Float3Type, length)
	nn.neuron = make([][]*neuron, length)
	for i, v := range nn.Weights {
		length = len(v)
		nn.weights[i] = make(pkg.Float2Type, length)
		nn.neuron[i] = make([]*neuron, length)
		for j, w := range v {
			nn.weights[i][j] = make(pkg.Float1Type, len(w))
			nn.neuron[i][j] = &neuron{}
		}
	}
}

// initCompletion.
func (nn *NN) initCompletion() {
	nn.input = make(pkg.Float1Type, nn.lenInput)
	nn.target = make(pkg.Float1Type, nn.lenOutput)
	nn.output = make([]float64, nn.lenOutput)
	nn.isInit = true
}
"""
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
