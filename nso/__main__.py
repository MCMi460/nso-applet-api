# Made by Deltaion Lee (MCMi460) on Github
from . import *

if __name__ == '__main__':
    from private import headers # Necessary for API requests
    # See template.private.py for more information regarding the private.py
    apiObject:NSOAppletAPI = NSOAppletAPI(headers = headers)
