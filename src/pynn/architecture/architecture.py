import json
import os.path as path
from typing import Any, Union, TypeVar

from pynn.architecture.hopfield.hopfield import Hopfield
from pynn.architecture.perceptron.perceptron import Perceptron

NN = Union[Perceptron, Hopfield]
T = TypeVar("T")
NNN = Perceptron | Hopfield

# iter_name = Perceptron.name, Hopfield.name
# print(type(iter_name))
# for i in iter_name:
#     print(i)
#
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
i = 0


def _architecture(reader: str, **props: Any) -> NNN:
    """
    Returns an instance of one of the architectures.
    """
    global i
    print(i)
    i += 1
    if reader.lower() == Perceptron.name:
        return Perceptron(**props)
    elif reader.lower() == Hopfield.name:
        return Hopfield(**props)
    else:
        if reader != "":
            props = _get_props_from(reader)

        if props != {}:
            if "name" in props:
                return _architecture(props["name"], **props)
            else:
                raise NameError("missing field: name")

    return Perceptron()


def _get_props_from(reader: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    if path.isfile(reader):
        filename = path.normpath(reader)
        _, extension = path.splitext(filename)
        if extension == ".json":
            with open(filename) as handle:
                data = json.load(handle)
            # data["config"] = filename
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
