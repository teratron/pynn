from abc import ABC, abstractmethod
from asyncio import Lock
from dataclasses import dataclass
from typing import Any, Optional, Callable


# from .architecture import Perceptron
# from .architecture import Hopfield

# class NeuralNetwork:
#     def __init__(self) -> None:
#         """Init"""
#         pass


@dataclass(slots=True, frozen=True)
class _Call:
    # class Callback(NamedTuple):
    call: Callable[[float], float]
    initialize: Callable[[Any, Any], None]
    set_props: Callable[[Any, Any], None]
    verify: Callable[[Any, Any], float]
    query: Callable[[Any, Any], list[float]]
    train: Callable[[Any, Any], tuple[int, float]]
    and_train: Callable[[Any, Any], tuple[int, float]]
    write: Callable[[Any, Any], None]


class Interface(ABC):  # metaclass=ABCMeta, Callback
    """Interface for neural network.
    """

    name: str = "interface"
    type: str = "Interface"
    description: str = __doc__

    is_init: bool = False
    config: Optional[str] = None
    mutex: Lock

    # weights: list[list[Union[list[float], float]]]

    # def __init_subclass__(cls, **props: Any) -> None:
    # super().__init_subclass__(**props)
    # print("__init_subclass__:", cls, props)

    #     # if "weights" in cls.props:
    #     #     self.weights = props["weights"]
    #     #     del props["weights"]

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

    # def __init__(self) -> None:
    #     self.call2 = call2

    # def call(self, args: float) -> float:
    #     print(self)
    #     if _Call.call is not None:
    #         return _Call.call(args)
    #     return 0

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

    def write(
            self,
            *,
            filename: str | None = None,
            flag: str | None = None,
            config: str | None = None,
            weights: str | None = None
    ) -> None:
        """Writes the configuration and weights to a file.

        * Записывает в один файл и конфигурацию и веса:
        write("perceptron.json")
        write(config="perceptron.json", weights="perceptron.json")

        * Записывает только конфигурацию:
        write(config="perceptron.json")
        write("perceptron.json", flag="config")

        * Записывает только веса:
        write(weights="perceptron_weights.json")
        write("perceptron.json", flag="weights")

        * Записывает 2 файла, конфигурацию отдельно и веса отдельно:
        write(config="perceptron.json", weights="perceptron_weights.json")
        """
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
