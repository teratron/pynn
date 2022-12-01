from .perceptron import Perceptron
#from .properties import Properties


class Pynn(Perceptron):
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(kwargs)

