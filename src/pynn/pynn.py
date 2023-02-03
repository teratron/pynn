from typing import Any

from pynn import activation
from pynn.properties import loss
# from pynn.architecture.architecture import architecture, NNN
from pynn.architecture.architecture import architecture


class Pynn(activation.Mode, loss.LossMode):
    """Access point to neural network.

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

    # def __new__(cls, reader: str = "", **props: Any) -> NNN:
    def __new__(cls, reader: str = "", **props: Any) -> Any:
        # arch = architecture(reader, **props)
        # if isinstance(arch, Perceptron):
        #     print(type(arch))
        # return super().__new__(Perceptron)
        return architecture(reader, **props)
