# Made by Deltaion Lee (MCMi460) on Github
from . import *

os.system('')
class Color:
    DEFAULT = '\033[0m'
    RED = '\033[91m'
    PURPLE = '\033[0;35m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WHITE = '\033[1;37m'

def toString(self, indent:int = 0) -> str:
    ret = []
    for key in dir(self):
        if not callable(getattr(self, key)) and not key.startswith('__'):
            value = self.__dict__[key]
            if hasattr(value, '__dict__'):
                value = '\n' + toString(value, indent + 1)
            if isinstance(value, list):
                value = '[\n' + ',\n\n'.join( (toString(object, indent + 1) if hasattr(object, '__dict__') else (('    ' * (indent + 1)) + str(object))) for object in value ) + '\n' + ('    ' * indent) + ']'
            ret.append((key, value))
    return ('    ' * indent) + 'Object: ' + type(self).__name__ + '\n' + '\n'.join([ ('    ' * indent) + '%s: %s' % (key, value) for key, value in ret ])
