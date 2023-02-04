from pynn.properties.activation import Activation
from pynn.properties.bias import Bias
from pynn.properties.layer import Layer, LayerType
from pynn.properties.loss import Loss
from pynn.properties.rate import Rate


class Properties(Bias, Layer, Activation, Loss, Rate):
    """Properties of neural network.
    """

    __slots__ = (
        "_name",
        "_bias",
        "_hidden_layers",
        "_activation_mode",
        "_loss_mode",
        "_loss_limit",
        "_rate"
    )

    def __init__(
            self,
            name: str,  # TODO: ?
            *,
            bias: bool = True,
            hidden_layers: LayerType = None,
            activation_mode: int = Activation.TANH,
            loss_mode: int = Loss.RMSE,
            loss_limit: float = 0.1e-3,
            rate: float = Rate.DEFAULT_RATE,
    ) -> None:
        self._name: str = name

        Layer.__init__(self, hidden_layers)
        Activation.__init__(self, activation_mode)
        Loss.__init__(self, loss_mode, loss_limit)
        Rate.__init__(self, rate)
        Bias.__init__(self, bias)
