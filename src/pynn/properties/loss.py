import math

from typing import Callable, Any, Iterable


class LossMode:
    """The mode of calculation of the total error:

    * MSE -- Mean Squared Error (0);
    * RMSE -- Root Mean Squared Error (1);
    * ARCTAN -- Arctan Error (2);
    * AVG -- Average Error (3).
    """

    MSE: int = 0
    """MSE -- Mean Squared Error (0)."""

    RMSE: int = 1
    """RMSE -- Root Mean Squared Error (1)."""

    ARCTAN: int = 2
    """ARCTAN -- Arctan Error (2)."""

    AVG: int = 3
    """AVG -- Average Error (3)."""


class Loss(LossMode):
    def __init__(
            self,
            /,
            loss_mode: int = LossMode.RMSE,
            loss_limit: float = 0.1e-3,
    ) -> None:
        self._loss_mode: int = loss_mode
        self._loss_limit: float = loss_limit

    @property
    def loss_mode(self) -> int:
        return self._loss_mode

    @loss_mode.setter
    def loss_mode(self, mode: int) -> None:
        self._loss_mode = loss.check(mode)

    @property
    def loss_limit(self) -> float:
        """Minimum (sufficient) limit of the average of the error during training."""
        return self._loss_limit

    @loss_limit.setter
    def loss_limit(self, limit: float) -> None:
        self._loss_limit = self._check_loss_limit(limit)

    @staticmethod
    def _check_loss_limit(limit: float) -> float:
        return 0.1e-6 if limit <= 0 else limit

    @classmethod
    def check(cls, mode: int) -> int:
        """Check loss mode."""
        return cls.MSE if mode > cls.AVG else mode


def loss(mode: int = Loss.MSE) -> Callable[[Callable[[], Any]], Callable[[], float]]:
    def outer(func: Callable[[], Any]) -> Callable[[], float]:
        def inner() -> float:
            _loss = 0.0
            miss = func()

            if isinstance(miss, Iterable):
                count = 0.0
                for value in miss:
                    _loss += __get_loss(value, mode)
                    count += 1

                if count > 1:
                    _loss /= count
            elif isinstance(miss, float):
                _loss += __get_loss(miss, mode)

            if mode == Loss.RMSE:
                _loss = math.sqrt(_loss)

            if math.isnan(_loss):
                raise ValueError('loss not-a-number value')

            if math.isinf(_loss):
                raise ValueError('loss is infinity')

            return _loss

        return inner

    return outer


def __get_loss(value: float, mode: int) -> float:
    match mode:
        case Loss.AVG:
            return math.fabs(value)
        case Loss.ARCTAN:
            return math.atan(value) ** 2
        case Loss.MSE | Loss.RMSE | _:
            return value ** 2

# @loss(0)
# def calc_loss() -> Iterable[float]:
#     for value in (0.27, -0.31, -0.52, 0.66, 0.81):
#         yield value
#
#
# @loss(2)
# def _calc_loss() -> float:
#     return 0.333
#
#
# if __name__ == "__main__":
#     print('calc_loss', calc_loss())
#     print('_calc_loss', _calc_loss())
