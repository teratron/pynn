# PYNN

## About

**pynn** - Neural Network Library

## Install

```shell
$ pip install pynn
```

## Getting Started

```python
import pynn

# New returns a new neural network
# instance with the default parameters.
n = pynn.new()

# Dataset.
data_input  = {.27, .31}
data_target = {.7}

# Training dataset.
_, _ = pynn.train(data_input, data_target)
```

## Documentation

More documentation is available at the [pynn website](https://teratron.github.io/pynn).

## Examples

You can find examples of neural networks in the 
[example's directory](https://github.com/teratron/pynn/tree/master/examples).
