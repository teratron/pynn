from architecture.perceptron import main as p


class NeuralNetwork:
    name: str = ''


class Pynn:
    def __init__(self):
        self.neural_network = p.Perceptron()

    # @property
    # def neural_network(self) -> object:
    #     return self.neural_network
    #
    # @neural_network.setter
    # def neural_network(self, value):
    #     self._neural_network = value

    def info(self):
        print(self.neural_network)


if __name__ == '__main__':
    per = Pynn()
    print(per.info())
