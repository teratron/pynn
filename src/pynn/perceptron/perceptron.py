import random

from .interface.interface import Interface
from .propagation.propagation import Propagation
from .properties import Properties


class Neuron:
    def __init__(self, value: float, miss: float):
        self.value = value
        self.miss = miss


class Perceptron(Interface, Propagation, Properties):
    """
    Perceptron is neural network.
    """

    name: str = 'perceptron'
    type: str = 'Perceptron'
    description: str = 'description'

    def __init__(self, **props):
        if 'name' in props:
            del props['name']

        # Weights
        self.weights: list[list[list[float]]]
        if 'weights' in props:
            self.weights = props['weights']
            del props['weights']
        else:
            self.weights = [
                [[random.uniform(-.5, .5) for _ in range(5)] for _ in range(5)] for _ in range(5)
            ]

        # Config
        if 'config' in props:
            self.config = props['config']
            del props['config']

        super().__init__(**props)

        # Neurons
        self.neurons: list[list[Neuron]] = [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]

        # Transfer data
        self.data_weight: list[list[list[float]]] = self.weights
        self.data_input: list[float] = [.1, .3]  # TODO:
        self.data_target: list[float] = [.1, .3]  # TODO:
        self.data_output: list[float] = [.1, .3]  # TODO:

        # Settings
        self.len_input: int = 2  # TODO:
        self.len_output: int = 2  # TODO:
        self.last_layer_ind: int = 1  # TODO:
        self.is_init: bool = False  # TODO:
        # self.mutex: sync.Mutex  # TODO:

    def __str__(self):
        return '%s.%s' % (self.__class__.__name__, self.name)

    def __repr__(self):
        return '<%s: %r>' % (self.__str__(), self.__dict__)

    def __dir__(self):
        """
        Returns all members and all public methods.
        """
        return ['__class__', '__doc__', '__module__'] + \
               [
                   m
                   for cls in self.__class__.mro()
                   for m in cls.__dict__
                   if m[0] != '_'
               ] + [m for m in self.__dict__ if m[0] != '_']
