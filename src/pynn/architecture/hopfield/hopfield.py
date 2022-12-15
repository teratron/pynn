from typing import Any

from pynn.interface import Interface


# from .properties import Properties


class Hopfield(Interface):
    """
    Hopfield is neural network.
    """

    name: str = "hopfield"
    type: str = "Hopfield"
    description: str = "description"

    def __init__(self, **props) -> None:
        super().__init__(**props)

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
