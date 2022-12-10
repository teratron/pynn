# from .pynn import *
# from .pynn import *
# from src.pynn import architecture

from pynn import architecture
from pynn import hopfield
from pynn import perceptron
from pynn import pynn
from pynn import version
from pynn.hopfield import hopfield
from pynn.perceptron import perceptron
from pynn.perceptron.perceptron import *
# from src.pynn.architecture import *
from src.pynn.pynn import *

# from . import activation
# sys.path.append(os.path.join('/home/oleg/Projects/src/github.com/teratron/pynn/src/pynn'))
# pprint(sys.path)
# pprint(sys.modules)
# __all__ = ['Pynn']

# Package version.
__version__ = version.__version__

print('name__init__:', __name__)
