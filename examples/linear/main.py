import src.pynn as nn

# New returns a new neural network
# instance with the default parameters,
# same n = nn.New("perceptron").
n = nn.New("perceptron")

# Parameters.
n.set_hidden_layer(3, 2)
n.set_activation_mode(pynn.LINEAR)
n.set_loss_mode(pynn.MSE)
n.set_loss_limit(.0001)

# Dataset that doesn't need to be scaled.
data_input = {10.6, -5, 200}
data_target = {5, -50.3}

# Training dataset.
print(n.train(data_input, data_target))

# Check the trained data, the result should be about [5 -50.3].
print(n.query(data_input))


def main():
    pass


if __name__ == '__main__':
    main()
