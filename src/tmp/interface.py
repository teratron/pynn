class Interface:
    def __init__(self, neural_network):
        self.neural_network = neural_network

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
