from typing import Any


def initialize(obj: object, *args: Any, **kwargs: Any) -> None:
    print("init", obj, args, kwargs)


def _call(a: float) -> float:
    return 4.5 * a


# def init_completion(obj: Perceptron) -> None:
#     obj.is_init = True


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
