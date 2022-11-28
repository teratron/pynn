from pynn.pynn import NeuralNetwork


class Perceptron(NeuralNetwork):
    # name: str = 'perceptron'

    def __init__(self, _neural_network):
        # super().__init__(Perceptron.name)
        super().__init__(_neural_network)
        self.name = 'perceptron'

        """The neuron bias, false or true (required field for a config)."""
        self.bias: bool = True

        """List of the number of neurons in each hidden layer."""
        self.hidden_layer: list = []

        """Activation function mode (required field for a config)."""
        self.activation_mode: int = 0

        """The mode of calculation of the total error."""
        self.loss_mode: int = 0

        """Minimum (sufficient) limit of the average of the error during training."""
        self.loss_limit: float = .0001

        """Learning coefficient (greater than 0 and less than or equal to 1)."""
        self.rate: float = .3

        """Weights of value."""
        self.weight: list[list[list[float]]] = []

    # @property
    # def bias(self) -> bool:
    #     return self.bias
    #
    # @bias.setter
    # def bias(self, bias: bool):
    #     self.bias = bias

    def init(self, *_data):
        pass

    def query(self, _data_input: list[float]) -> list[float]:
        return [.1]

    def verify(self, _data_input: list[float], *_data_target: list[float]) -> float:
        return .1

    def train(self, _data_input: list[float], *_data_target: list[float]) -> (int, float):
        return 0, .1

    def and_train(self, _data_target: list[float]) -> (int, float):
        return 0, .1

    def write_config(self, *_filename: str) -> Exception:
        return Exception(None)

    def write_weights(self, _filename: str) -> Exception:
        return Exception(None)
