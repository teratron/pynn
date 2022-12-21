import json
import os.path as path
from typing import Any, Union, TypeVar

from pynn.architecture.hopfield.hopfield import Hopfield
from pynn.architecture.perceptron.perceptron import Perceptron

NN = Union[Perceptron, Hopfield]
T = TypeVar("T")
NNN = Perceptron | Hopfield


# iter_name = Iterable[Union[Perceptron, Hopfield]]
# NN = TypeVar("NN", Perceptron, Hopfield)
# for i in iter_name:
# print(i)


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


def architecture(reader: str, **props: Any) -> NNN:
    """
    Returns an instance of one of the architectures.
    """

    # 2
    if reader != "" and props == {}:
        if reader.lower() == Perceptron.name:
            return Perceptron()
        elif reader.lower() == Hopfield.name:
            return Hopfield()
        else:
            props = _get_props_from(reader)
            if props != {} and "name" in props:
                if props["name"] == Perceptron.name:
                    return Perceptron(**props)
                elif props["name"] == Hopfield.name:
                    return Hopfield(**props)
                else:
                    raise NameError(props["name"])  # TODO: text

    # 3
    if reader != "" and props != {}:
        if reader.lower() == Perceptron.name:
            if "name" in props and props["name"] != Perceptron.name:
                raise NameError(props["name"])  # TODO: text
            return Perceptron(**props)
        elif reader.lower() == Hopfield.name:
            if "name" in props and props["name"] != Hopfield.name:
                raise NameError(props["name"])  # TODO: text
            return Hopfield(**props)
        else:
            props = _get_props_from(reader)
            if props != {} and "name" in props:
                if props["name"] == Perceptron.name:
                    return Perceptron(**props)
                elif props["name"] == Hopfield.name:
                    return Hopfield(**props)
                else:
                    raise NameError(props["name"])  # TODO: text

    # 4
    if reader == "" and props != {} and "name" in props:
        if props["name"] == Perceptron.name:
            return Perceptron(**props)
        elif props["name"] == Hopfield.name:
            return Hopfield(**props)
        else:
            raise NameError(props["name"])  # TODO: text

    # if reader != "":
    #     if reader.lower() == Perceptron.name:
    #         return Perceptron(**props)
    #     elif reader.lower() == Hopfield.name:
    #         return Hopfield(**props)
    #     else:
    #         data: dict[str, Any]
    #         filename = path.normpath(reader)
    #         if path.isfile(filename):
    #             _, extension = path.splitext(filename)
    #             if extension == ".json":
    #                 with open(filename) as handle:
    #                     data = json.load(handle)
    #                 data["config"] = filename
    #             else:
    #                 raise FileExistsError("")  # TODO: text
    #         else:
    #             data = json.loads(reader)
    #             data["config"] = None
    #
    #         if "name" in data:
    #             return architecture(data["name"], **data)

    # 1
    return Perceptron()


# del json


# def _sd(name: str, call):
#     if name.lower() == Perceptron.name:
#         call()
#     elif name.lower() == Hopfield.name:
#         return Hopfield()


def _get_props_from(reader: str) -> dict[str, Any]:
    data: dict[str, Any]
    filename = path.normpath(reader)
    if path.isfile(filename):
        _, extension = path.splitext(filename)
        if extension == ".json":
            with open(filename) as handle:
                data = json.load(handle)
            data["config"] = filename
        else:
            raise FileExistsError("")  # TODO: text
    else:
        data = json.loads(reader)

    return data
