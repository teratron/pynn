from typing import Any

from pynn import activation, loss
from pynn.architecture.architecture import _architecture, NNN


class Pynn(activation.Mode, loss.Mode):
    """
    Access point to neural network.

    Pynn(reader: str, **kwargs)

    Examples:
        - Pynn()
        - Pynn("perceptron")
        - Pynn("perceptron", bias=True, rate=0.3)
        - Pynn(name="perceptron", bias=True, rate=0.3)
        - Pynn("config/perceptron.json")
        - Pynn("{'name': 'perceptron', 'bias': true, 'rate': 0.3}")
        - Pynn(**{"name": "perceptron", "bias": True, "rate": 0.3})

    Keyword arguments:

    reader -- string variable through which is passed:
        - Name of the neural network ("perceptron" or "hopfield");
        - Filename of json config ("config.json");
        - Directly json dump passed as a string ("{'name': 'perceptron', ...}").
    **kwargs -- properties of the neural network.
    """

    # @overload
    # def __new__(cls, reader: str, **props: Any) -> Perceptron: ...
    #
    # @overload
    # def __new__(cls, reader: str, **props: Any) -> Hopfield: ...

    def __new__(cls, reader: str = "", **props: Any) -> NNN:
        # print(cls)
        # arch = _architecture(reader, **props)
        # if isinstance(arch, Perceptron):
        #     print(type(arch))
        # return super().__new__(Perceptron)
        return _architecture(reader, **props)
