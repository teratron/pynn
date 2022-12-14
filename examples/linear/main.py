from pynn import Pynn

if __name__ == "__main__":
    # Returns a new neural network
    # instance with the default parameters,
    # same n = nn.New("perceptron").
    pn = Pynn()

    # Properties.
    pn.hidden_layers = [3, 2]
    pn.activation_mode = pn.LINEAR
    pn.loss_mode = pn.MSE
    pn.loss_limit = 0.0001

    # Dataset that doesn't need to be scaled.
    data_input = [10.6, -5, 200]
    data_target = [5, -50.3]

    # Training dataset.
    print(pn.train(data_input, data_target))

    # Check the trained data, the result should be about [5 -50.3].
    print(pn.query(data_input))
