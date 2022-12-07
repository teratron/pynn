import pynn.activation as activation
import pynn.architecture as architecture
import pynn.loss as loss

from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


class Pynn(activation.Mode, loss.Mode):
    """
    Pynn.

    reader - String variable through which is passed:
        - Name of the neural network;
        - Filename of json config;
        - Directly json dump passed as a string.
    """

    def __new__(cls, reader: str = '', **kwargs) -> Perceptron | Hopfield | Exception:
        instance = architecture.get(reader)
        if not isinstance(instance, FileExistsError):
            instance.__init__(reader, **kwargs)
        print('instance:', instance)
        return instance
