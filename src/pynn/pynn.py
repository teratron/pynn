from typing import Any

from pynn import activation, loss
from .architecture import architecture


class Pynn(activation.Mode, loss.Mode):
    """
    Access point

    Pynn(reader: str, **kwargs)

    Examples:
        - Pynn()
        - Pynn('perceptron')
        - Pynn('config/perceptron.json')
        - Pynn('{"name": "perceptron", ...}')

    Keyword arguments:

    reader -- string variable through which is passed (default ""):
        - Name of the neural network ('perceptron' | 'hopfield' | ...);
        - Filename of json config ('config.json');
        - Directly json dump passed as a string ('{"name": "perceptron", ...}').
    **kwargs -- properties of the neural network.
    """

    def __new__(cls, reader: str = "", **kwargs: Any):
        return architecture(reader, **kwargs)
