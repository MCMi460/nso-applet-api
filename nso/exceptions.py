# Made by Deltaion Lee (MCMi460) on Github
from . import *

class NSOAppletAPI_Exception(Exception):
    def __init__(self, message:str, data:str = '') -> None:
        self.log(data, 'NSOAppletAPI_Exception: ' + message)
        super().__init__(message)

    def log(self, *text:list) -> None:
        print(Color.RED + 'Custom traceback:\n' + Color.YELLOW + '\n'.join(map(str, text)) + Color.DEFAULT)
