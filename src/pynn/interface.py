from abc import ABC
from typing import Tuple, Any, List, Callable, Dict


class Properties(ABC):
    pass


class Parameters(ABC):
    pass


class Interface(Properties, Parameters):
    """
    Interface for neural network.
    """

    def __init__(self,
                 init: Callable[[object], None],
                 props: Callable[[object, Dict[str, Any]], None],
                 verify: Callable[[object, List[float], List[float]], float],
                 query: Callable[[object, List[float]], List[float]],
                 train: Any,
                 and_train: Any,
                 write_config: Any,
                 write_weights: Any):
        self._props = props
        self._init = init
        self._verify = verify
        self._query = query
        self._train = train
        self._and_train = and_train
        self._write_config = write_config
        self._write_weights = write_weights

    def _initialize(self) -> None:
        """Initialize neural network."""
        self._init(self)

    def props(self, **kwargs: Dict[str, Any]) -> None:
        """Set properties of neural network."""
        self._props(self, kwargs)

    def verify(self, data_input: List[float], data_target: List[float]) -> float:
        """Verifying dataset."""
        return self._verify(self, data_input, data_target)

    def query(self, data_input: List[float]) -> List[float]:
        """Querying dataset."""
        return self._query(self, data_input)

    def train(self, data_input: List[float], data_target: List[float]) -> Tuple[int, float]:
        """Training dataset."""
        return self._train(self, data_input, data_target)

    def and_train(self, data_target: List[float]) -> Tuple[int, float]:
        """Training dataset after the query."""
        return self._and_train(self, data_target)

    def write_config(self, filename: str) -> Exception:
        """Writes the configuration and weights to a file."""
        return self._write_config(self, filename)

    def write_weights(self, filename: str) -> Exception:
        """Writes weights to a file."""
        return self._write_weights(self, filename)
