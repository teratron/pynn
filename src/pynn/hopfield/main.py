#from pynn.pynn import NeuralNetwork


class Hopfield:
    name: str = 'hopfield'

    # def __init__(self):
    #     pass
    # def info(self):
    #     print('hopfield')
    @staticmethod
    def query(data_input: list[float]) -> list[float]:
        print('percept', data_input)
        return data_input

    def verify(self, _data_input: list[float], *_data_target: list[float]) -> float:
        return .1

    def train(self, _data_input: list[float], *_data_target: list[float]) -> (int, float):
        return 0, .1

    def and_train(self, _data_target: list[float]) -> (int, float):
        return 0, .1

    def write_config(self, *_filename: str) -> Exception:
        return Exception(None)

    def write_weights(self, _filename: str) -> Exception:
        return Exception(None)
