import math
from typing import Callable, Any


class Mode:
    """
    The mode of calculation of the total error:
    MSE -- Mean Squared Error (0);
    RMSE -- Root Mean Squared Error (1);
    ARCTAN -- Arctan Error (2);
    AVG -- Average Error (3).
    """

    MSE: int = 0
    """MSE -- Mean Squared Error (0)."""

    RMSE: int = 1
    """RMSE -- Root Mean Squared Error (1)."""

    ARCTAN: int = 2
    """ARCTAN -- Arctan Error (2)."""

    AVG: int = 3
    """AVG -- Average Error (3)."""


def check(mode: int) -> int:
    """Check loss mode."""
    return Mode.MSE if mode > Mode.AVG else mode


def loss(mode: int = Mode.MSE) -> Callable[[Callable[[], Any]], Callable[[], float]]:
    def outer(func: Callable[[], Any]) -> Callable[[], float]:  # Union[Generator, float]
        def inner() -> float:
            _loss = count = 0.0
            # if isinstance(func, Generator):
            for value in func():
                _loss += _get_loss(value, mode)
                count += 1

            if count > 1:
                _loss /= count

            if mode == Mode.RMSE:
                _loss = math.sqrt(_loss)

            if math.isnan(_loss):
                raise ValueError('loss not-a-number value')

            if math.isinf(_loss):
                raise ValueError('loss is infinity')

            return _loss

        return inner

    return outer


def _get_loss(value: float, mode: int) -> float:
    match mode:
        case Mode.AVG:
            return math.fabs(value)
        case Mode.ARCTAN:
            return math.atan(value) ** 2
        case Mode.MSE | Mode.RMSE | _:
            return value ** 2


@loss(0)
def calc_loss() -> Any:  # -> Generator
    for value in (0.27, -0.31, -0.52, 0.66, 0.81):
        yield value


if __name__ == "__main__":
    print('calc_loss', calc_loss())
