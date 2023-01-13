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


class Perceptron(Interface, Properties, Parameters, Propagation):
    """
    Perceptron is neural network.
    """

    print("Perceptron")
    name: str = "perceptron"
    type: str = "Perceptron"
    description: str = __doc__

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
        # print("props", props)
        # Properties.__init__(self, self.name, **props)
        Properties.__init__(self, **props)
        # Parameters.__init__(self)
        Propagation.__init__(self, self)

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
