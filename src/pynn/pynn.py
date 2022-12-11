import pynn.activation as activation
import pynn.architecture as architecture
import pynn.loss as loss


class Pynn(activation.Mode, loss.Mode):
    """
    Pynn(reader, **properties).

    reader - String variable through which is passed:
        - Name of the neural network;
        - Filename of json config;
        - Directly json dump passed as a string.
    """

    def __new__(cls, reader: str = '', **kwargs):
        return architecture.get(reader, **kwargs)
