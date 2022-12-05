import random

import pynn.activation as act
import pynn.loss as loss


class Neuron:
    def __init__(self, value: float, miss: float):
        self.value = value
        self.miss = miss


class Properties(act.Mode, loss.Mode):
    """
    Properties.
    """

    def __init__(self,
                 *,
                 bias: bool = True,
                 hidden_layers=None,
                 activation_mode: int = act.Mode.SIGMOID,
                 loss_mode: int = loss.Mode.RMSE,
                 loss_limit: float = .1e-3,
                 rate: float = .3):
        self._bias: bool = bias
        """The neuron bias, false or true (required field for a config)."""

        self._hidden_layers: list[int] = Properties.check_hidden_layers(hidden_layers)
        """List of the number of neuron in each hidden layers."""

        self._activation_mode: int = act.check(activation_mode)
        """Activation function mode (required field for a config)."""

        self._loss_mode: int = loss.check(loss_mode)
        """The mode of calculation of the total error."""

        self._loss_limit: float = loss_limit
        """Minimum (sufficient) limit of the average of the error during training."""

        self._rate: float = Properties.check_rate(rate)
        """Learning coefficient (greater than 0.0 and less than or equal to 1.0)."""

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
        self.data_weight: list[list[list[float]]] = self.weight
        self.data_input: list[float] = [.1, .3]  # TODO:
        self.data_target: list[float] = [.1, .3]  # TODO:
        self.data_output: list[float] = [.1, .3]  # TODO:

        # super().__init__(self)

    # Bias
    @property
    def bias(self) -> bool:
        """
        The neuron bias, false or true (required field for a config).
        """
        return self._bias

    @bias.setter
    def bias(self, bias: bool):
        self._bias = bias

    # Hidden layers
    @property
    def hidden_layers(self) -> list[int]:
        """
        List of the number of neuron in each hidden layers.
        """
        return self._hidden_layers

    @hidden_layers.setter
    def hidden_layers(self, layers: list[int]):
        self._hidden_layers = Properties.check_hidden_layers(layers)

    @staticmethod
    def check_hidden_layers(layers: list[int]) -> list[int]:
        return [0] if layers is None else layers

    # Activation mode
    @property
    def activation_mode(self) -> int:
        """
        Activation function mode:
            LINEAR - Linear/identity (0);
            RELU - ReLu (rectified linear unit) (1);
            LEAKY_RELU - Leaky ReLu (leaky rectified linear unit) (2);
            SIGMOID - Logistic, a.k.a. sigmoid or soft step (3);
            TANH - TanH (hyperbolic tangent) (4).
        """
        return self._activation_mode

    @activation_mode.setter
    def activation_mode(self, mode: int):
        self._activation_mode = act.check(mode)

    # Loss mode
    @property
    def loss_mode(self) -> int:
        """
        The mode of calculation of the total error:
            MSE - Mean Squared Error (0);
            RMSE - Root Mean Squared Error (1);
            ARCTAN - Arctan Error (2);
            AVG - Average Error (3).
        """
        return self._loss_mode

    @loss_mode.setter
    def loss_mode(self, mode: int):
        self._loss_mode = loss.check(mode)

    # Loss limit
    @property
    def loss_limit(self) -> float:
        """
        Minimum (sufficient) limit of the average of the error during training.
        """
        return self._loss_limit

    @loss_limit.setter
    def loss_limit(self, limit: float):
        self._loss_limit = Properties.check_loss_limit(limit)

    @staticmethod
    def check_loss_limit(limit: float) -> float:
        return .1e-6 if limit <= 0 else limit

    # Rate
    @property
    def rate(self) -> float:
        """
        Learning coefficient (greater than 0.0 and less than or equal to 1.0).
        """
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = Properties.check_rate(rate)

    @staticmethod
    def check_rate(rate: float) -> float:
        return .3 if rate <= 0 or rate > 1 else rate