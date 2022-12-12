from typing import Tuple


class _Interface:
    """
    Interface for neural network.
    """

    def __init__(self, props, init, verify, query, train, and_train, write_config, write_weights):
        self._props = props
        self._init = init
        self._verify = verify
        self._query = query
        self._train = train
        self._and_train = and_train
        self._write_config = write_config
        self._write_weights = write_weights
        print('int2:', self.init.__name__, self.__class__.__mro__)

    def props(self, **kwargs) -> None:
        """Set properties of neural network."""
        self._props(self, **kwargs)

    def init(self) -> None:
        """Initialize neural network."""
        self._init(self)

    def verify(self, data_input: list[float], data_target: list[float]) -> float:
        """
        Verifying dataset.
        """
        return self._verify(data_input, data_target)

    def query(self, data_input: list[float]) -> list[float]:
        """
        Querying dataset.
        """
        return self._query(self, data_input)

    def train(self, data_input: list[float], data_target: list[float]) -> Tuple[int, float]:
        """Training dataset."""
        return self._train(self, data_input, data_target)

    def and_train(self, data_target: list[float]) -> Tuple[int, float]:
        """Training dataset after the query."""
        return self._and_train(self, data_target)

    def write_config(self, filename: str) -> Exception:
        """Writes the configuration and weights to a file."""
        return self._write_config(self, filename)

    def write_weights(self, filename: str) -> Exception:
        """Writes weights to a file."""
        return self._write_weights(self, filename)
