from abc import ABC
from typing import Any, Callable


class Properties(ABC):
    pass


class Parameters(ABC):
    pass


class Interface(Properties, Parameters):
    """
    Interface for neural network.
    """

    def __init__(self,
                 call_init: Callable[[object, tuple[Any, ...], dict[str, Any]], None],
                 call_props: Callable[[object, tuple[Any, ...], dict[str, Any]], None],
                 call_verify: Callable[[object, tuple[Any, ...], dict[str, Any]], float],
                 call_query: Callable[[object, tuple[Any, ...], dict[str, Any]], list[float]],
                 call_train: Callable[[object, tuple[Any, ...], dict[str, Any]], tuple[int, float]],
                 call_and_train: Callable[[object, tuple[Any, ...], dict[str, Any]], tuple[int, float]],
                 call_write: Callable[[object, tuple[Any, ...], dict[str, Any]], None]):
        self._call_init = call_init
        self._call_props = call_props
        self._call_verify = call_verify
        self._call_query = call_query
        self._call_train = call_train
        self._call_and_train = call_and_train
        self._call_write = call_write

        # pprint.pprint(self._call__dict__)

    def _initialize(self, *args: Any, **kwargs: Any) -> None:
        """Initialize neural network."""
        self._call_init(self, *args, **kwargs)

    def props(self, *args: Any, **kwargs: Any) -> None:
        """Set properties of neural network."""
        self._call_props(self, *args, **kwargs)

    def verify(self, *args: Any, **kwargs: Any) -> float:
        """Verifying dataset."""
        return self._call_verify(self, *args, **kwargs)

    def query(self, *args: Any, **kwargs: Any) -> list[float]:
        """Querying dataset."""
        return self._call_query(self, *args, **kwargs)

    def train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset."""
        return self._call_train(self, *args, **kwargs)

    def and_train(self, *args: Any, **kwargs: Any) -> tuple[int, float]:
        """Training dataset after the query."""
        return self._call_and_train(self, *args, **kwargs)

    def write(self, *args: Any, **kwargs: Any) -> None:
        """Writes the configuration and weights to a file."""
        self._call_write(self, *args, **kwargs)

    @classmethod
    def dust(cls, *args: Any, **kwargs: Any) -> None:
        cls.dust(*args, **kwargs)
