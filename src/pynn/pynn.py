from typing import Any

from pynn import activation, loss
from .architecture import architecture


class Pynn(activation.Mode, loss.Mode):
    """
    Access point

    Pynn(reader: str, **kwargs)

    Examples:
        Pynn()
        Pynn('perceptron')
        Pynn('config/perceptron.json')
        Pynn('{"name": "perceptron", ...}')

    Keyword arguments:
    reader -- (default "")
    Examples: "" | 'perceptron' | 'hopfield' | 'config.json' | '{"name": "perceptron", ...}'
    String variable through which is passed:
        - Name of the neural network;
        - Filename of json config;
        - Directly json dump passed as a string.

    **kwargs -- properties of the neural network.
    """

    def __new__(cls, reader: str = "", **kwargs: Any) -> Any:
        return architecture(reader, **kwargs)
