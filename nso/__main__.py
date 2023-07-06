# Made by Deltaion Lee (MCMi460) on Github
from . import *

if __name__ == '__main__':
    from private import headers # Necessary for API requests -- see template.private.py for more information regarding the private.py
    apiObject:NSOAppletAPI = NSOAppletAPI(headers = headers)

    print(Color.RED, end = '')
    print('You are now entering an \'execution\' zone. Any and all user input will be exec()-ed, so beware.')

    try:
        import readline
    except ImportError:
        pass
    while True:
        print(Color.YELLOW, end = '')
        print('API Endpoints: ' + ', '.join( 'apiObject.' + e for e in dir(NSOAppletAPI) if not e.startswith('_') ))
        print(Color.DEFAULT, end = '')
        endpoint = input('>>> ' + Color.WHITE)
        exec(endpoint, globals(), locals())
