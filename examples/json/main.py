import pynn

# New returns a new neural network from config.
n = pynn.new(join("config", "perceptron.json"))

# Dataset.
data_input = {1, 1}
data_target = {0}

# Training dataset.
_, _ = n.train(data_input, data_target)

# Writing weights to a file.
_ = n.write_weight("perceptron_weights.json")
