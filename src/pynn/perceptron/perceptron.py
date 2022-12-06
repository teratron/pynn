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

    def __init__(self, reader, **kwargs):
        super().__init__(reader, **kwargs)

        # Weights
        self.weight: list[list[list[float]]] = [
            [[random.uniform(-.5, .5) for _ in range(5)] for _ in range(5)] for _ in range(5)
        ]

        # Neurons
        self.neuron: list[list[Neuron]] = [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]

        # Settings
        self.len_input: int = 2  # TODO:
        self.len_output: int = 2  # TODO:
        self.last_layer_ind: int = 1
        self.is_init: bool = False
        # self.config         utils.Filer
        # self.mutex          sync.Mutex

        # Transfer data
        self.data_weight: list[list[list[float]]] = self.weight
        self.data_input: list[float] = [.1, .3]  # TODO:
        self.data_target: list[float] = [.1, .3]  # TODO:
        self.data_output: list[float] = [.1, .3]  # TODO:

    def __repr__(self):
        return '<%s.%s: %r>' % (self.__class__.__name__, self.name, self.description)

    def __str__(self):
        return '%s.%s' % (self.__class__.__name__, self.name)

    def __dir__(self):
        """
        Returns all members and all public methods.
        """
        added_behavior = [
                             m
                             for cls in self.__class__.mro()
                             for m in cls.__dict__
                             if m[0] != '_'
                         ] + [m for m in self.__dict__ if m[0] != '_']
        return ['__class__', '__doc__', '__module__'] + added_behavior
