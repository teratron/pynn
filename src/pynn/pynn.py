from pynn.architecture._architecture import _architecture
from .utils import loss, activation


class Pynn(activation.Mode, loss.Mode):
    """
    Pynn(reader: str, **kwargs)

    Examples:
        Pynn()
        Pynn('perceptron')
        Pynn('config/perceptron.json')
        Pynn('{"name": "perceptron", ...}')

    reader = '' | 'perceptron' | 'hopfield' | 'config.json' | '{"name": "perceptron", ...}'
        String variable through which is passed:
        - Name of the neural network;
        - Filename of json config;
        - Directly json dump passed as a string.

    **kwargs - properties of the neural network.
    """

    def __new__(cls, reader: str = '', **kwargs):
        return _architecture(reader, **kwargs)
