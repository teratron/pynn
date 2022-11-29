from .architecture import get_architecture


# class Properties:
#     pass
#
#
# class NeuralNetwork(Interface, Properties):
#     name: str
#
#     # properties: Properties
#     def __init__(self, neural_network):
#         #super().__init__(neural_network)
#         #self.interface = Interface('')
#         pass


class Pynn:
    def __init__(self, name: str):
        self.name = name
        self.neural_network = get_architecture(self.name)

    def init(self, *args):
        self.neural_network.init(args)

    def query(self, data_input: list[float]) -> list[float]:
        print('Interface')
        return self.neural_network.query(data_input)

    def verify(self, data_input: list[float], *data_target: list[float]) -> float:
        return self.neural_network.verify(data_input, data_target)

    def train(self, data_input: list[float], *data_target: list[float]) -> (int, float):
        return self.neural_network.train(data_input, data_target)

    def and_train(self, data_target: list[float]) -> (int, float):
        return self.neural_network.and_train(data_target)

    def write_config(self, *filename: str) -> Exception:
        return self.neural_network.write_config(filename)

    def write_weights(self, filename: str) -> Exception:
        return self.neural_network.write_weights(filename)

    def info(self):
        print(self.name, self.neural_network)
