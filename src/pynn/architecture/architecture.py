import json
import os
from typing import Any, Union

from pynn.architecture.hopfield.hopfield import Hopfield
from pynn.architecture.perceptron.perceptron import Perceptron

# NNN = Union[Perceptron]
NNN = Union[Perceptron, Hopfield]


# NNN = Perceptron | Hopfield

# *- Pynn()
#
# *- Pynn("perceptron")
# - Pynn("perceptron", name="perceptron", bias=True, rate=0.3)
# - Pynn("perceptron", **{"name": "perceptron", "bias": True, "rate": 0.3})
#
# *- Pynn("config.json")
# - Pynn("config.json", name="perceptron", bias=True, rate=0.3)
# - Pynn("config.json", **{"name": "perceptron", "bias": True, "rate": 0.3})
#
# *- Pynn("{'name': 'perceptron', 'bias': true, 'rate': 0.3}")
# - Pynn("{'name': 'perceptron', 'bias': true, 'rate': 0.3}", name="perceptron", bias=True, rate=0.3)
# - Pynn("{'name': 'perceptron', 'bias': true, 'rate': 0.3}", **{"name": "perceptron", "bias": True, "rate": 0.3})
#
# *- Pynn(name="perceptron", bias=True, rate=0.3)
# *- Pynn(**{"name": "perceptron", "bias": True, "rate": 0.3})

# @staticmethod  #: Union[Perceptron, Hopfield]
# def trim_props(self, **props: Any) -> dict[str, Any]:
#     # if "name" in props:
#     #     del props["name"]
#
#     if "weights" in props:
#         self.weights = props["weights"]
#         del props["weights"]
#
#     if "config" in props:
#         self.config = props["config"]
#         del props["config"]
#
#     return props

#i = 0


def architecture(reader: str, **props: Any) -> NNN:
    """
    Returns an instance of one of the architectures.
    """
    # global i
    # print(i)
    # i += 1
    if reader.lower() == Perceptron.name:
        return Perceptron(**props)
    elif reader.lower() == Hopfield.name:
        return Hopfield(**props)
    else:
        if reader != "":
            props = _get_props_from(reader)

        if props != {}:
            if "name" in props:
                return architecture(props["name"], **props)
            else:
                raise NameError("missing field: name")

    return Perceptron()


def _get_props_from(reader: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    if os.path.isfile(reader):
        filename = os.path.normpath(reader)
        _, extension = os.path.splitext(filename)
        if extension == ".json":
            with open(filename) as handle:
                data = json.load(handle)
            data.update(config=filename)
            print(data)
        else:
            raise FileExistsError("incorrect config file extension: " + extension)
    else:
        try:
            data = json.loads(reader)
        except json.JSONDecodeError as err:
            print("JSONDecodeError", err)

    return data
