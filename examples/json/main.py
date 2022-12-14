import os.path as path

from pynn import Pynn

if __name__ == "__main__":
    # Returns a new neural network instance from config.
    pn = Pynn(path.join("config", "perceptron.json"))

    # Dataset.
    data_input = [1.0, 1.0]
    data_target = [0.0]

    # Training dataset.
    _, _ = pn.train(data_input, data_target)

    # Writing weights to a file.
    _ = pn.write(weights="perceptron_weights.json")
