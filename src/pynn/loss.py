class Mode:
    """
    The mode of calculation of the total error:

    MSE - Mean Squared Error (0);
    RMSE - Root Mean Squared Error (1);
    ARCTAN - Arctan Error (2);
    AVG - Average Error (3).
    """

    MSE: int = 0
    """MSE - Mean Squared Error (0)."""

    RMSE: int = 1
    """RMSE - Root Mean Squared Error (1)."""

    ARCTAN: int = 2
    """ARCTAN - Arctan Error (2)."""

    AVG: int = 3
    """AVG - Average Error (3)."""


def check(mode: int) -> int:
    """
    Check loss mode.
    """
    return Mode.MSE if mode > Mode.AVG else mode

# def error(value: float, mode: int = Mode.MSE, *args: tuple[float]):
#     """
#     Calculating and return the total error of the output neurons.
#     """
#     # TODO: try-catch
#     print(args)
#     _loss = 0.
#     for i in range(len_output):
#         miss[i] = target[i] - value[i]
#         match mode:
#             case Mode.MSE, Mode.RMSE, _:
#                 _loss += miss[i] ** 2
#             case Mode.ARCTAN:
#                 _loss += math.atan(miss[i]) ** 2
#             case Mode.AVG:
#                 _loss += math.fabs(miss[i])
#
#     _loss /= len_output
#     if mode == Mode.RMSE:
#         _loss = math.sqrt(_loss)
#
#     match True:
#         case math.isnan(_loss):
#             logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
#         case math.isinf(_loss):
#             logging.log(0, 'perceptron.calc_loss: loss is infinity')
#
#     yield _loss
