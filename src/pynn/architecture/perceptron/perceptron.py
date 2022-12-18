import random
from typing import Any

from pynn.architecture.perceptron.interface.initialize import initialize
from pynn.architecture.perceptron.interface.query import query
from pynn.architecture.perceptron.interface.set_props import set_props
from pynn.architecture.perceptron.interface.train import train, and_train
from pynn.architecture.perceptron.interface.verify import verify
from pynn.architecture.perceptron.interface.write import write
from pynn.architecture.perceptron.parameters import Parameters
from pynn.architecture.perceptron.propagation import Propagation
from pynn.architecture.perceptron.properties import Properties
from pynn.interface import Interface


# from pynn.interface import NeuralNetwork


# from .interface import initialize
# from .interface import set_props
# from .interface import query
# from .interface import train, and_train
# from .interface import verify
# from .interface import write
# from .parameters import Parameters
# from .propagation import Propagation
# #from .properties import Properties


class Perceptron(Interface, Properties, Parameters, Propagation):
    """
    Perceptron is neural network.
    """

    name: str = "perceptron"
    type: str = "Perceptron"
    description: str = "description"

    def __init__(self, **props: Any) -> None:
        # if "name" in props:
        #     del props["name"]

        # Weights
        if "weights" in props:
            self.weights = props["weights"]
            del props["weights"]
        else:
            self.weights = [
                [[random.uniform(-0.5, 0.5) for _ in range(5)] for _ in range(5)]
                for _ in range(5)
            ]

        # Config
        if "config" in props:
            self.config = props["config"]
            del props["config"]

        # props = super().trim_props(self, **props)
        Properties.__init__(self, **props)

        # super().__init__(**props)
        # del props["name"]
        # del props["weights"]
        # del props["config"]
        # Properties.__init__(self, **props)

        # Interface.__init__(self, initialize, set_props, verify, query, train, and_train, write)
        # Propagation.__init__(self, self)

        # Neurons, type: list[list[Neuron]]
        # self.neurons = [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]
        #
        # # Transfer data
        # self.data_weight = self.weights
        # self.data_input = [.1, .3]  # TODO:
        # self.data_target = [.1, .3]  # TODO:
        # self.data_output = [.1, .3]  # TODO:
        #
        # # Settings
        # self.len_input = 2  # TODO:
        # self.len_output = 2  # TODO:
        # self.last_layer_ind = 1  # TODO:
        # self.is_init = False  # TODO:
        # # self.mutex: sync.Mutex  # TODO:

    def _initialize(self, *args: Any, **kwargs: Any) -> None:
        """Initialize neural network."""
        initialize(self, *args, **kwargs)

    def set_props(self, *args: Any, **kwargs: Any) -> None:
        """Set properties of neural network."""
        set_props(self, *args, **kwargs)

    def verify(self, *args: Any, **kwargs: Any) -> float:
        """Verifying dataset."""
        return verify(self, *args, **kwargs)

    def query(self, *args: Any, **kwargs: Any) -> list[float]:
        """Querying dataset."""
        return query(self, args, **kwargs)

    def train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset."""
        return train(self, *args, **kwargs)

    def and_train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset after the query."""
        return and_train(self, *args, **kwargs)

    def write(self, *args: Any, **kwargs: Any) -> None:
        """Writes the configuration and weights to a file."""
        write(self, *args, **kwargs)
