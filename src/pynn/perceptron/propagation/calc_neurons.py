import pynn.activation as act


def calc_neurons(obj) -> None:
    print('+-*/*-+')  # TODO:
    length, dec = obj.len_input, 0
    for i in range(len(obj.neuron)):
        if i > 0:
            dec = i - 1
            length = len(obj.neuron[dec])

        for j in range(len(obj.neuron[i])):
            obj.neuron[i][j].value = num = 0.
            for k in range(len(obj.data_weight[i][j])):
                if k < length:
                    if i > 0:
                        obj.neuron[i][j].value += obj.neuron[dec][k].value * obj.data_weight[i][j][k]
                    else:
                        obj.neuron[i][j].value += obj.data_input[k] * obj.data_weight[i][j][k]
                else:
                    obj.neuron[i][j].value += obj.data_weight[i][j][k]
                num += 1

            if obj.activation_mode == obj.LINEAR:
                if num > 0:
                    obj.neuron[i][j].value /= num
            else:
                obj.neuron[i][j].value = act.activation(obj.neuron[i][j].value, obj.activation_mode)
