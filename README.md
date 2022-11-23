# PYNN

https://docs.pipenv.org/advanced/#configuration-with-environment-variables
https://webdevblog.ru/pipenv-rukovodstvo-po-novomu-instrumentu-python/
https://pypi.org/project/pipenv/#usage-examples
https://habr.com/ru/company/piter/blog/700282/

https://habr.com/ru/post/122082/
https://habr.com/ru/post/560300/
https://www.sphinx-doc.org/en/master/

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
