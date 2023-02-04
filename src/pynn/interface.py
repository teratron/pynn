from abc import ABC, abstractmethod
from asyncio import Lock
from typing import Any, Optional


# from .architecture import Perceptron
# from .architecture import Hopfield

# class NeuralNetwork:
#     def __init__(self) -> None:
#         """Init"""
#         pass


class Interface(ABC):  # metaclass=ABCMeta
    """Interface for neural network.
    """

    name: str = "interface"
    type: str = "Interface"
    description: str = __doc__

    is_init: bool = False
    config: Optional[str] = None
    mutex: Lock

    # weights: list[list[Union[list[float], float]]]

    def __init_subclass__(cls, **props: Any) -> None:
        super().__init_subclass__(**props)
        print("__init_subclass__:", cls, props)
        # if "weights" in cls.props:
        #     self.weights = props["weights"]
        #     del props["weights"]

    # def trim_props(self, **props: Any) -> dict[str, Any]:
    #     # if "name" in props:
    #     #     del props["name"]
    #
    #     if "weights" in props:
    #         self.weights = props["weights"]
    #         del props["weights"]
    #
    #     if "config" in props:
    #         self.config = props["config"]
    #         del props["config"]
    #
    #     return props

    @abstractmethod
    def _initialize(self, *args: Any, **kwargs: Any) -> None:
        """Initialize neural network."""
        ...

    @abstractmethod
    def set_props(self, *args: Any, **kwargs: Any) -> None:
        """Set properties of neural network."""
        ...

    @abstractmethod
    def verify(self, *args: Any, **kwargs: Any) -> float:
        """Verifying dataset."""
        ...

    @abstractmethod
    def query(self, *args: Any, **kwargs: Any) -> list[float]:
        """Querying dataset."""
        ...

    @abstractmethod
    def train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset."""
        ...

    @abstractmethod
    def and_train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset after the query."""
        ...

    @abstractmethod
    def write(self, *args: Any, **kwargs: Any) -> None:
        """Writes the configuration and weights to a file."""
        ...

    def __str__(self) -> str:
        return "%s.%s" % (self.__class__.__name__, self.name)

    def __repr__(self) -> str:
        return "<%s: %r>" % (self.__str__(), self.__dict__)

    def __dir__(self) -> list[str]:
        """Returns all members and all public methods."""
        return (
                ["__class__", "__doc__", "__module__"] +
                [m for cls in self.__class__.mro() for m in cls.__dict__ if m[0] != "_"] +
                [m for m in self.__dict__ if m[0] != "_"]
        )
