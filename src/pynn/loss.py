import math


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


def error(mode: int = Mode.MSE):
    def outer(func):
        print('decorator outer')

        def inner():
            print('decorator inner')
            _loss = count = 0.0
            # for i in range(len_output):
            for i in range(1):
                # miss[i] = target[i] - value[i]
                _loss += _get_loss(0.0 + i, mode) + 2
                func()
                count += 1

            if count > 1:
                _loss /= count

            if mode == Mode.RMSE:
                _loss = math.sqrt(_loss)

            # match True:
            #     case math.isnan(_loss):
            #         logging.log(0, 'loss not-a-number value')
            #         raise ValueError('loss not-a-number value')
            #     case math.isinf(_loss):
            #         logging.log(0, 'loss is infinity')
            #         raise ValueError('loss is infinity')

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
            print('Mode.MSE | Mode.RMSE | _')
            return value ** 2


@error(0)
def calc_loss() -> float:
    print('decorator')
    return 1.0


if __name__ == "__main__":
    print('calc_loss', calc_loss())
