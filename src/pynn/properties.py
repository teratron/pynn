class Properties:
    def __init__(self,
                 *,
                 bias: bool = True,
                 hidden_layer=None,
                 activation_mode: int = 0,
                 loss_mode: int = 0,
                 loss_limit: float = .0001,
                 rate: float = .3):
        """The neuron bias, false or true (required field for a config)."""
        self.bias: bool = bias

        """List of the number of neurons in each hidden layer."""
        self.hidden_layer: list[int] = [] if hidden_layer is None else hidden_layer

        """Activation function mode (required field for a config)."""
        self.activation_mode: int = activation_mode

        """The mode of calculation of the total error."""
        self.loss_mode: int = loss_mode

        """Minimum (sufficient) limit of the average of the error during training."""
        self.loss_limit: float = loss_limit

        """Learning coefficient (greater than 0 and less than or equal to 1)."""
        self.rate: float = rate

        """Weights of value."""
        self.weights: list[list[list[float]]] = [
            [[.1 for _ in range(10)] for _ in range(10)] for _ in range(10)
        ]

    # @property
    # def bias(self) -> bool:
    #     return self.bias
    #
    # @bias.setter
    # def bias(self, bias: bool):
    #     self.bias = bias
