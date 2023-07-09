# Made by Deltaion Lee (MCMi460) on Github
from . import *

if __name__ == '__main__':
    from private import headers # Necessary for API requests -- see template.private.py for more information regarding the private.py
    with NSOAppletAPI(headers = headers) as api:
        print(Color.RED + 'You are now entering an \'execution\' zone. Any and all user input will be exec()-ed, so beware.')
        print(Color.YELLOW + 'API Endpoints: ' + ', '.join( 'api.' + e for e in dir(NSOAppletAPI) if not e.startswith('_') ))
        print(Color.DEFAULT, end = '')

        try:
            import readline
        except ImportError:
            pass
        while True:
            endpoint:str = input('>>> ' + Color.WHITE)
            exec(endpoint, globals(), locals())
