import pynn.activation as act


def calc_neurons(obj) -> None:
    print('+-*/*-+')  # TODO:
    length, dec = obj.len_input, 0
    for i in range(len(obj.neurons)):
        if i > 0:
            dec = i - 1
            length = len(obj.neurons[dec])

        for j in range(len(obj.neurons[i])):
            obj.neurons[i][j].value = num = 0.
            for k in range(len(obj.data_weight[i][j])):
                if k < length:
                    if i > 0:
                        obj.neurons[i][j].value += obj.neurons[dec][k].value * obj.data_weight[i][j][k]
                    else:
                        obj.neurons[i][j].value += obj.data_input[k] * obj.data_weight[i][j][k]
                else:
                    obj.neurons[i][j].value += obj.data_weight[i][j][k]
                num += 1

            if obj.activation_mode == obj.LINEAR:
                if num > 0:
                    obj.neurons[i][j].value /= num
            else:
                obj.neurons[i][j].value = act.activation(obj.neurons[i][j].value, obj.activation_mode)
