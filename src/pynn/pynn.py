# from architecture.perceptron.main import Perceptron


class Interface:
    def __init__(self, neural_network):
        self.neural_network = neural_network  # Perceptron()

    def init(self, *_data):
        self.neural_network.init(1, 2)

    def query(self, _data_input: list[float]) -> list[float]:
        return self.neural_network.query([.2])

    def verify(self, _data_input: list[float], *_data_target: list[float]) -> float:
        return self.neural_network.verify([.2], [])

    def train(self, _data_input: list[float], *_data_target: list[float]) -> (int, float):
        return self.neural_network.train([.2], [])

    def and_train(self, _data_target: list[float]) -> (int, float):
        return self.neural_network.and_train([.2])

    def write_config(self, *_filename: str) -> Exception:
        return self.neural_network.write_config('')

    def write_weights(self, _filename: str) -> Exception:
        return self.neural_network.write_weights('')


class Properties:
    pass


class NeuralNetwork(Interface, Properties):
    name: str

    # properties: Properties
    def __init__(self, neural_network):
        super().__init__(neural_network)
        self.interface = Interface('')


class Pynn:
    def __init__(self, name: str = ''):
        self.name = name
        # self.neural_network = #Perceptron()

    # @property
    # def neural_network(self) -> object:
    #     return self.neural_network
    #
    # @neural_network.setter
    # def neural_network(self, value):
    #     self._neural_network = value

    def info(self):
        print(self.name)


if __name__ == '__main__':
    per = Pynn()
    print(per.info())
