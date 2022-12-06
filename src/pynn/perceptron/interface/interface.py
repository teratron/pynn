from .init import init
from .query import query
from .set import set
from .train import train, and_train
from .verify import verify
from .write import write_config, write_weights


class Interface:
    """
    Interface.
    """

    def set(self, **kwargs) -> None:
        """
        Set properties of neural network.
        """
        set(self, **kwargs)

    def init(self, *args) -> None:
        """
        Initialize neural network.
        """
        init(self, *args)

    def verify(self, data_input: list[float], data_target: list[float]) -> float:
        """
        Verifying dataset.
        """
        return verify(self, data_input, data_target)

    def query(self, data_input: list[float]) -> list[float]:
        """
        Querying dataset.
        """
        return query(self, data_input)

    def train(self, data_input: list[float], data_target: list[float]) -> (int, float):
        """
        Training dataset.
        """
        return train(self, data_input, data_target)

    def and_train(self, data_target: list[float]) -> (int, float):
        """
        Training dataset after the query.
        """
        return and_train(self, data_target)

    def write_config(self, filename: str) -> Exception:
        """
        Writes the configuration and weights to a file.
        """
        return write_config(self, filename)

    def write_weights(self, filename: str) -> Exception:
        """
        Writes weights to a file.
        """
        return write_weights(self, filename)
