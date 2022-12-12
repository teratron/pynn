import math


class Mode:
    """
    Activation function mode:
    LINEAR - Linear/identity (0);
    RELU - ReLu (rectified linear unit) (1);
    LEAKY_RELU - Leaky ReLu (leaky rectified linear unit) (2);
    SIGMOID - Logistic, a.k.a. sigmoid or soft step (3);
    TANH - TanH (hyperbolic tangent) (4).
    """

    LINEAR: int = 0
    """LINEAR - Linear/identity (0)."""

    RELU: int = 1
    """RELU - ReLu (rectified linear unit) (1)."""

    LEAKY_RELU: int = 2
    """LEAKY_RELU - Leaky ReLu (leaky rectified linear unit) (2)."""

    SIGMOID: int = 3
    """SIGMOID - Logistic, a.k.a. sigmoid or soft step (3)."""

    TANH: int = 4
    """TANH - TanH (hyperbolic tangent) (4)."""


def check(mode: int) -> int:
    """Check activation mode."""
    return Mode.SIGMOID if mode > Mode.TANH else mode


def activation(value: float, mode: int = Mode.SIGMOID) -> float:
    """Activation function."""
    match mode:
        case Mode.LINEAR:
            return value
        case Mode.RELU:
            return .0 if value < 0 else value
        case Mode.LEAKY_RELU:
            return .01 * value if value < 0 else value
        case Mode.SIGMOID, _:
            return 1 / (1 + math.exp(-value))
        case Mode.TANH:
            value = math.exp(2 * value)
            return (value - 1) / (value + 1)


def derivative(value: float, mode: int = Mode.SIGMOID) -> float:
    """Derivative activation function."""
    match mode:
        case Mode.LINEAR:
            return 1
        case Mode.RELU:
            return 0 if value < 0 else 1
        case Mode.LEAKY_RELU:
            return .01 if value < 0 else 1
        case Mode.SIGMOID, _:
            return value * (1 - value)
        case Mode.TANH:
            return 1 - value ** 2
