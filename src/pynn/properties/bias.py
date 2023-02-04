class Bias:
    """Bias.

    The neuron bias, false or true (required field for a config).
    """

    def __init__(self, bias: bool) -> None:
        self._bias: bool = bias

    @property
    def bias(self) -> bool:
        return self._bias

    @bias.setter
    def bias(self, value: bool) -> None:
        self._bias = value
