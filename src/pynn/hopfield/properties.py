import pynn.activation as activation
import pynn.loss as loss


class Properties(activation.Mode, loss.Mode):
    """
    Properties of neural network.
    """

    def __init__(self,
                 *,
                 energy: float = .3):
        self._energy: float = Properties.check_energy(energy)
        """Energy."""

    @property
    def energy(self) -> float:
        """
        Energy.
        """
        return self._energy

    @energy.setter
    def energy(self, energy: float):
        self._energy = Properties.check_energy(energy)

    @staticmethod
    def check_energy(energy: float) -> float:
        return .3 if energy <= 0 or energy > 1 else energy
