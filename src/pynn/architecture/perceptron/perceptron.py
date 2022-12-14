from typing import Any

# from pynn.interface import Interface
from pynn.interface2 import Interface2
# from .interface import init
# from .interface import props
# from .interface import query
# from .interface import train, and_train
# from .interface import verify
# from .interface import write
from .parameters import Parameters
from .propagation import Propagation
from .properties import Properties


# from .interface import init, props, verify, query, train, and_train, write


class Perceptron(Interface2, Properties, Parameters, Propagation):
    """
    Perceptron is neural network.
    """

    name: str = "perceptron"
    type: str = "Perceptron"
    description: str = "description"

    def __init__(self, **kwargs: Any):
        # if "name" in kwargs:
        #     del kwargs["name"]
        #
        # # Weights
        # if "weights" in kwargs:
        #     self.weights = kwargs["weights"]
        #     del kwargs["weights"]
        # else:
        #     self.weights = [
        #         [[random.uniform(-0.5, 0.5) for _ in range(5)] for _ in range(5)]
        #         for _ in range(5)
        #     ]
        #
        # # Config
        # if "config" in kwargs:
        #     self.config = kwargs["config"]
        #     del kwargs["config"]

        props = super().strip_props(self, **kwargs)
        Properties.__init__(self, **props)
        # super().__init__(**props)

        # Interface.__init__(self, init, props, verify, query, train, and_train, write)
        # Propagation.__init__(self, self)

        # self.dust(*args, **kwargs)
        #     dust(*args, **kwargs)

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
        pass

    def set_props(self, *args: Any, **kwargs: Any) -> None:
        """Set properties of neural network."""
        pass

    def verify(self, *args: Any, **kwargs: Any) -> float:
        """Verifying dataset."""
        pass

    def query(self, *args: Any, **kwargs: Any) -> list[float]:
        """Querying dataset."""
        pass

    def train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset."""
        pass

    def and_train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset after the query."""
        pass

    def write(self, *args: Any, **kwargs: Any) -> None:
        """Writes the configuration and weights to a file."""
        pass
