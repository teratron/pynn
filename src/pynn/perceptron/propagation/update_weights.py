import pynn.activation as act


def update_weights(obj) -> None:
    """
    Update weights.
    """
    length, dec = obj.len_input, 0
    for i in range(len(obj.data_weight)):
        if i > 0:
            dec = i - 1
            length = len(obj.neuron[dec])

        for j in range(len(obj.data_weight[i])):
            grad = obj.rate * obj.neuron[i][j].miss * act.derivative(obj.neuron[i][j].value, obj.activation_mode)
            for k in range(len(obj.data_weight[i][j])):
                if k < length:
                    val: float
                    if i > 0:
                        val = obj.neuron[dec][k].value
                    else:
                        val = obj.data_input[k]

                    if obj.activation_mode == obj.LINEAR:
                        if val != 0:
                            obj.data_weight[i][j][k] += grad / val
                    else:
                        obj.data_weight[i][j][k] += grad * val
                else:
                    obj.data_weight[i][j][k] += grad
