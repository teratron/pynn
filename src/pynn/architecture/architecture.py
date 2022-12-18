import json
import os.path as path
from typing import Any, Union, TypeVar

from pynn.architecture.hopfield.hopfield import Hopfield
from pynn.architecture.perceptron.perceptron import Perceptron
from pynn.interface import Interface

NN = Union[Perceptron, Hopfield]
T = TypeVar("T")
NNN = Perceptron | Hopfield


# NN = TypeVar("NN", Perceptron, Hopfield)


def architecture(reader: str, **props: Any) -> Interface:
    """
    Returns an instance of one of the architectures.
    """
    if reader != "":
        if reader.lower() == Perceptron.name:
            return Perceptron(**props)
        elif reader.lower() == Hopfield.name:
            return Hopfield(**props)
        else:
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
                data["config"] = None

            if "name" in data:
                return architecture(data["name"], **data)

    return Perceptron()

# del json
