from .interface import Interface


class Neuron:
    def __init__(self, value: float, miss: float):
        self.value = value
        self.miss = miss


class Perceptron(Interface):
    name: str = 'perceptron'
    type: str = 'Perceptron'
    description: str = ''

    """Weights of value."""
    weights: list[list[list[float]]] = [
        [[.1 for _ in range(10)] for _ in range(10)] for _ in range(10)
    ]

    """Neurons."""
    neurons: list[list[Neuron]] = []

    """Settings."""
    len_input: int
    len_output: int
    last_layer_index: int
    is_init: bool = False
    # config         utils.Filer
    # mutex          sync.Mutex

    """Transfer data."""
    transfer_weight: list[list[list[float]]]
    transfer_input: list[float]
    transfer_target: list[float]
    transfer_output: list[float]

    def __init__(self):
        super().__init__()
    #     """The neuron bias, false or true (required field for a config)."""
    #     self.bias: bool = True
    #
    #     """List of the number of neurons in each hidden layer."""
    #     self.hidden_layer: list = []
    #
    #     """Activation function mode (required field for a config)."""
    #     self.activation_mode: int = 0
    #
    #     """The mode of calculation of the total error."""
    #     self.loss_mode: int = 0
    #
    #     """Minimum (sufficient) limit of the average of the error during training."""
    #     self.loss_limit: float = .0001
    #
    #     """Learning coefficient (greater than 0 and less than or equal to 1)."""
    #     self.rate: float = .3
    #
    #     """Weights of value."""
    #     self.weights: list[list[list[float]]] = []

    # @property
    # def bias(self) -> bool:
    #     return self.bias
    #
    # @bias.setter
    # def bias(self, bias: bool):
    #     self.bias = bias

    # def init(self, *args):
    #     pass
    #
    # def query(self, data_input: list[float]) -> list[float]:
    #     print('percept', data_input)
    #     # q(data_input)
    #     return data_input
    #
    # def verify(self, _data_input: list[float], *_data_target: list[float]) -> float:
    #     return .1
    #
    # def train(self, _data_input: list[float], *_data_target: list[float]) -> (int, float):
    #     return 0, .1
    #
    # def and_train(self, _data_target: list[float]) -> (int, float):
    #     return 0, .1
    #
    # def write_config(self, *_filename: str) -> Exception:
    #     return Exception(None)
    #
    # def write_weights(self, _filename: str) -> Exception:
    #     return Exception(None)
