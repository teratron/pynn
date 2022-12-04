import random

import pynn.activation as act
import pynn.loss as loss
from .propagation import Propagation
from .query import query
from .train import train, and_train
from .verify import verify
from .write import write_config, write_weights


# import json
# json.JSONDecoder


class Neuron:
    def __init__(self, value: float, miss: float):
        self.value = value
        self.miss = miss


class Perceptron(Propagation, act.Mode, loss.Mode):
    """
    Perceptron is neural network
    """
    name: str = 'perceptron'
    type: str = 'Perceptron'
    description: str = 'description'  # Perceptron.__doc__()

    def __init__(self,
                 *,
                 bias: bool = True,
                 hidden_layers=None,
                 activation_mode: int = act.Mode.SIGMOID,
                 loss_mode: int = loss.Mode.RMSE,
                 loss_limit: float = .1e-3,
                 rate: float = .3):
        """The neuron bias, false or true (required field for a config)."""
        self._bias: bool = bias

        """List of the number of neuron in each hidden layers."""
        self._hidden_layers: list[int] = Perceptron.check_hidden_layers(hidden_layers)

        """Activation function mode (required field for a config)."""
        self._activation_mode: int = act.check(activation_mode)

        """The mode of calculation of the total error."""
        self._loss_mode: int = loss.check(loss_mode)

        """Minimum (sufficient) limit of the average of the error during training."""
        self._loss_limit: float = loss_limit

        """Learning coefficient (greater than 0 and less than or equal to 1)."""
        self._rate: float = Perceptron.check_rate(rate)

        # Weights
        self.weight: list[list[list[float]]] = [
            [[random.uniform(-.5, .5) for _ in range(5)] for _ in range(5)] for _ in range(5)
        ]

        # Neurons
        self.neuron: list[list[Neuron]] = [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]

        # Settings
        self.len_input: int = 2  # TODO:
        self.len_output: int = 2  # TODO:
        self.last_layer_ind: int = 1
        self.is_init: bool = False
        # self.config         utils.Filer
        # self.mutex          sync.Mutex

        # Transfer data
        self.transfer_weight: list[list[list[float]]] = self.weight
        self.transfer_input: list[float] = [.1, .3]  # TODO:
        self.transfer_target: list[float] = [.1, .3]  # TODO:
        self.transfer_output: list[float] = [.1, .3]  # TODO:

        super().__init__(self)

    # def calc_neurons(self):
    #     super(Perceptron, self).calc_neurons(self)

    # Bias
    @property
    def bias(self) -> bool:
        return self._bias

    @bias.setter
    def bias(self, bias: bool):
        self._bias = bias

    # Hidden layers
    @property
    def hidden_layers(self) -> list[int]:
        return self._hidden_layers

    @hidden_layers.setter
    def hidden_layers(self, layers: list[int]):
        self._hidden_layers = Perceptron.check_hidden_layers(layers)

    @staticmethod
    def check_hidden_layers(layers: list[int]) -> list[int]:
        return [0] if layers is None else layers

    # Activation mode
    @property
    def activation_mode(self) -> int:
        return self._activation_mode

    @activation_mode.setter
    def activation_mode(self, mode: int):
        self._activation_mode = act.check(mode)

    # Loss mode
    @property
    def loss_mode(self) -> int:
        return self._loss_mode

    @loss_mode.setter
    def loss_mode(self, mode: int):
        self._loss_mode = loss.check(mode)

    # Loss limit
    @property
    def loss_limit(self) -> float:
        return self._loss_limit

    @loss_limit.setter
    def loss_limit(self, limit: float):
        self._loss_limit = Perceptron.check_loss_limit(limit)

    @staticmethod
    def check_loss_limit(limit: float) -> float:
        return .1e10 if limit <= 0 else limit

    # Rate
    @property
    def rate(self) -> float:
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = Perceptron.check_rate(rate)

    @staticmethod
    def check_rate(rate: float) -> float:
        return .3 if rate <= 0 or rate > 1 else rate

    # Interface
    def init(self, *args):
        # self.neural_network.init(args)
        pass

    def verify(self, data_input: list[float], data_target: list[float]) -> float:
        """
        Verifying dataset.
        """
        return verify(self, data_input, data_target)

    def query(self, data_input: list[float]) -> list[float]:
        """
        Querying dataset.
        """
        return query(self, data_input)

    def train(self, data_input: list[float], data_target: list[float]) -> (int, float):
        """
        Training dataset.
        """
        return train(self, data_input, data_target)

    def and_train(self, data_target: list[float]) -> (int, float):
        """
        Training dataset after the query.
        """
        return and_train(self, data_target)

    def write_config(self, filename: str) -> Exception:
        """
        Writes the configuration and weights to the Filer interface object.
        """
        return write_config(self, filename)

    def write_weights(self, filename: str) -> Exception:
        return write_weights(self, filename)

    def __repr__(self):
        return '<%s.%s: %r>' % (self.__class__.__name__, Perceptron.name, Perceptron.description)

    def __str__(self):
        return '%s.%s' % (self.__class__.__name__, Perceptron.name)

    def __dir__(self):
        """
        Returns all members and all public methods
        """
        added_behavior = [
                             m
                             for cls in self.__class__.mro()
                             for m in cls.__dict__
                             if m[0] != '_'
                         ] + [m for m in self.__dict__ if m[0] != '_']
        return ['__class__', '__doc__', '__module__'] + added_behavior


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
