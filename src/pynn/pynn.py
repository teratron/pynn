import pynn.activation as activation
import pynn.loss as loss
from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


class Pynn(activation.Mode, loss.Mode):
    """
    Pynn.
    """

    def __new__(cls, **kwargs):
        print(Hopfield)
        instance = super().__new__(Perceptron)
        instance.__init__(**kwargs)
        return instance

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
