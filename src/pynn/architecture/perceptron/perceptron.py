import random

from pynn.interface import Interface
from .interface import (props, init, verify, query, train, and_train, write_config, write_weights)
from .propagation import Propagation
from .properties import Properties


class Neuron:
    def __init__(self, value: float, miss: float):
        self.value = value
        self.miss = miss


class Perceptron(Properties, Interface, Propagation):
    """
    Perceptron is neural network.
    """

    name: str = 'perceptron'
    type: str = 'Perceptron'
    description: str = 'description'

    def __init__(self, **kwargs):
        if 'name' in kwargs:
            del kwargs['name']

        # Weights, type: list[list[list[float]]]
        if 'weights' in kwargs:
            self.weights = kwargs['weights']
            del kwargs['weights']
        else:
            self.weights = [
                [[random.uniform(-.5, .5) for _ in range(5)] for _ in range(5)] for _ in range(5)
            ]

        # Config
        if 'config' in kwargs:
            self.config = kwargs['config']
            del kwargs['config']

        super().__init__(**kwargs)
        Interface.__init__(self, props, init, verify, query, train, and_train, write_config, write_weights)
        Propagation.__init__(self, self)

        # Neurons, type: list[list[Neuron]]
        self.neurons = [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]

        # Transfer data
        self.data_weight = self.weights
        self.data_input = [.1, .3]  # TODO:
        self.data_target = [.1, .3]  # TODO:
        self.data_output = [.1, .3]  # TODO:

        # Settings
        self.len_input = 2  # TODO:
        self.len_output = 2  # TODO:
        self.last_layer_ind = 1  # TODO:
        self.is_init = False  # TODO:
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
