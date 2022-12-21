# PyNN

    Under construction

## About

Neural network library for python.

## Install

```shell
$ pip install pynn
```

## Getting Started

```python
from pynn import Pynn

if __name__ == '__main__':
    # Returns a new neural network
    # instance with the default parameters.
    pn = Pynn()

    # Dataset.
    data_input  = [0.27, 0.31]
    data_target = [0.7]

    # Training dataset.
    _, _ = pn.train(data_input, data_target)
```

## Documentation

More documentation is available at the [pynn website](https://teratron.github.io/pynn).

## Examples

You can find examples of neural networks in the 
[example's directory](https://github.com/teratron/pynn/tree/master/examples).
