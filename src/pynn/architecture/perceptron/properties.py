from typing import Optional

from pynn import loss, activation


class Properties:
    """
    Properties of neural network.
    """

    DEFAULT_RATE: float = 0.3

    __slots__ = (
        "_name",
        "_bias",
        "_hidden_layers",
        "_activation_mode",
        "_loss_mode",
        "_loss_limit",
        "_rate",
    )

    def __init__(
            self,
            name: str,
            *,
            bias: bool = True,
            hidden_layers: Optional[list[int]] = None,
            activation_mode: int = activation.Mode.TANH,
            loss_mode: int = loss.Mode.RMSE,
            loss_limit: float = 0.1e-3,
            rate: float = DEFAULT_RATE
    ) -> None:
        self._name: str = name
        self._bias: bool = bias
        self._hidden_layers: list[int] = Properties._check_hidden_layers(hidden_layers)
        self._activation_mode: int = activation.check(activation_mode)
        self._loss_mode: int = loss.check(loss_mode)
        self._loss_limit: float = loss_limit
        self._rate: float = Properties._check_rate(rate)

    @property
    def bias(self) -> bool:
        """The neuron bias, false or true (required field for a config)."""
        return self._bias

    @bias.setter
    def bias(self, bias: bool) -> None:
        self._bias = bias

    @property
    def hidden_layers(self) -> list[int]:
        """List of the number of neuron in each hidden layers."""
        return self._hidden_layers

    @hidden_layers.setter
    def hidden_layers(self, layers: list[int]) -> None:
        self._hidden_layers = Properties._check_hidden_layers(layers)

    @staticmethod
    def _check_hidden_layers(layers: Optional[list[int]]) -> list[int]:
        return [0] if layers is None else layers

    @property
    def activation_mode(self) -> int:
        """
        Activation function mode:
        LINEAR -- Linear/identity (0);
        RELU -- ReLu (rectified linear unit) (1);
        LEAKY_RELU -- Leaky ReLu (leaky rectified linear unit) (2);
        SIGMOID -- Logistic, a.k.a. sigmoid or soft step (3);
        TANH -- TanH (hyperbolic tangent) (4).
        """
        return self._activation_mode

    @activation_mode.setter
    def activation_mode(self, mode: int) -> None:
        self._activation_mode = activation.check(mode)

    @property
    def loss_mode(self) -> int:
        """
        The mode of calculation of the total error:
        MSE -- Mean Squared Error (0);
        RMSE -- Root Mean Squared Error (1);
        ARCTAN -- Arctan Error (2);
        AVG -- Average Error (3).
        """
        return self._loss_mode

    @loss_mode.setter
    def loss_mode(self, mode: int) -> None:
        self._loss_mode = loss.check(mode)

    @property
    def loss_limit(self) -> float:
        """Minimum (sufficient) limit of the average of the error during training."""
        return self._loss_limit

    @loss_limit.setter
    def loss_limit(self, limit: float) -> None:
        self._loss_limit = Properties._check_loss_limit(limit)

    @staticmethod
    def _check_loss_limit(limit: float) -> float:
        return 0.1e-6 if limit <= 0 else limit

    @property
    def rate(self) -> float:
        """Learning coefficient (greater than 0.0 and less than or equal to 1.0)."""
        return self._rate

    @rate.setter
    def rate(self, rate: float) -> None:
        self._rate = Properties._check_rate(rate)

    @classmethod
    def _check_rate(cls, rate: float) -> float:
        return cls.DEFAULT_RATE if rate <= 0 or rate > 1 else rate


# p = Properties(name='per')


# def compare_dictionaries(dict1, dict2) -> bool:
#     if dict1 is None or dict2 is None:
#         return False
#
#     if not isinstance(dict1, dict) or not isinstance(dict2, dict):
#         return False
#
#     shared_keys = set(dict1.keys()) & set(dict2.keys())
#
#     if not (len(shared_keys) == len(dict1.keys()) and len(shared_keys) == len(dict2.keys())):
#         print('Not all keys are shared')
#         return False
#
#     dicts_are_equal = True
#     for key in dict1.keys():
#         if isinstance(dict1[key], dict) or isinstance(dict2[key], dict):
#             dicts_are_equal = dicts_are_equal and compare_dictionaries(dict1[key], dict2[key])
#         else:
#             dicts_are_equal = dicts_are_equal and all(atleast_1d(dict1[key] == dict2[key]))
#
#     return dicts_are_equal


def dict_compare(d1, d2):
    print("&keys", set(d1.keys()) & set(d2.keys()))
    print("&items", set(d1.items()) & set(d2.items()))

    print("^keys", set(d2.keys()) ^ set(d1.keys()))
    print("^items", set(d2.items()) ^ set(d1.items()))

    print("|keys", set(d2.keys()) | set(d1.keys()))
    print("|items", set(d2.items()) | set(d1.items()))

    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    _added = d1_keys - d2_keys
    _removed = d2_keys - d1_keys
    _modified = {i: (d1[i], d2[i]) for i in shared_keys if d1[i] != d2[i]}
    _same = set(i for i in shared_keys if d1[i] == d2[i])

    return _added, _removed, _modified, _same


if __name__ == "__main__":
    x = dict(a=1, b=2, c=5, d=3)
    y = dict(a=2, b=2, d=0)
    added, removed, modified, same = dict_compare(x, y)
    print(added, removed, modified, same)
