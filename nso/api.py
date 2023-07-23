# Made by Deltaion Lee (MCMi460) on Github
from . import *

class NSOAppletAPI:
    def __init__(self, *, headers:dict = None, country:str = 'US') -> None:
        X_Api_Token = self.authorize(headers = headers) # Set X_Api_Token

        self.host = 'https://lp1.nso.nintendo.net'
        self.Session = httpx.Client(verify = False)
        self.Session.headers.update({
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Referer': 'https://lp1.nso.nintendo.net',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519',
            'X-Api-Token': X_Api_Token,
        })

        cookies = self.getV1Cookies(country) # Set cookies for the future
        self.expiry = cookies.expires

    def __enter__(self):
        self._log('[OK]', 'Initialized self', color = Color.GREEN)
        return self

    def __exit__(self, type, value, traceback):
        self.Session.close()
        self._log('[OK]', 'Closed Session', color = Color.GREEN)

    def _log(self, *text:str, color:str = Color.WHITE) -> None:
        print(color + ' '.join(map(str, text)) + Color.DEFAULT)

    def _formatQueryString(self, route:str, query:dict) -> str:
        return route + '?' + '&'.join( '%s=%s' % (key, query[key]) for key in query.keys() )

    def _get(self, route:str, *, query:dict = {}) -> httpx.Response:
        route = route.replace(self.host, '')
        if query:
            route = self._formatQueryString(route, query)

        self._log('[GET]', route)

        result = self.Session.get(self.host + route)
        self._log('[GET]', route, '<Response Code [%s]>' % result.status_code)
        return result

    def _post(self, route:str, *, query:dict = {}) -> httpx.Response:
        route = route.replace(self.host, '')
        if query:
            route = self._formatQueryString(route, query)

        self._log('[POST]', route)

        result = self.Session.post(self.host + route)
        self._log('[POST]', route, '<Response Code [%s]>' % result.status_code)
        return result

    ### AUTHORIZATION ROUTE ###

    def authorize(self, *, headers:dict = None) -> str:
        if not headers:
            raise NSOAppletAPI_Exception('missing authorization token generator headers')
        url = 'https://accounts.nintendo.com'
        route = '/connect/1.0.0/authorize?client_id=f4e5f2f3e022208b&response_type=id_token&scope=openid&redirect_uri=nintendo://lhub.nx.sys&state=a'

        self._log('[GET]', url + route)

        auth = requests.get(
            url + route,
            headers = headers,
            allow_redirects = False
        ) # Simulate logging in. Steal the request headers from an actual request to the same URL.
        # See template.private.py for more information regarding the private.py
        self._log('[GET]', url + route, '<Response Code [%s]>' % auth.status_code)

        data = urllib.parse.parse_qs(urllib.parse.urldefrag(auth.headers['location']).fragment)

        return data['id_token'][0]

    ### API ROUTES ###
    ## Disclaimer:
    ## I do not necessarily have all of the information regarding these endpoints
    ## If you get a return value that differs from mine on one of these,
    ## please make a new issue to tell me!
    ## Thanks! - MCMi460
    ## Note:
    ## I will also note beside endpoints that require an NSO membership
    ## in order to operate.
    def getUserInfo(self, country:str) -> User_Info:
        """GET - Gets the user's info

        Parameters
        ----------
        country : str
        the account's country code

        Returns
        -------
        User_Info
        an object with the user's info
        """
        return User_Info(**self._get('/api/v1/user/profile',
            query = {
                'country': country,
            }
        ).json())

    def getV1Cookies(self, country:str) -> Cookie:
        """GET - Stores the following cookies: CloudFront-Key-Pair-Id, CloudFront-Policy, CloudFront-Signature

        Parameters
        ----------
        country : str
        the account's country code

        Returns
        -------
        Cookie
        an object that contains the expiry information
        """
        return Cookie(**self._get('/api/v1/cookies',
            query = {
                'country': country,
            }
        ).json())

    def v1PostLogin(self, country:str) -> dict:
        """POST - Posts a login

        Parameters
        ----------
        country : str
        the account's country code

        Returns
        -------
        Login
        an object that contains information regarding the user's My Nintendo point balance
        """
        return Login(**self._post('/api/v1/login',
            query = {
                'country': country,
            }
        ).json())

    def getV1LClassicsTitles(self, statuses:str, country:str) -> list:
        """GET - Gets the current titles available under NSO's emulation softwares

        Parameters
        ----------
        statuses : str
        correlates to statuses[] - commonly is 'published'
        country : str
        the account's country code

        Returns
        -------
        list
            Classic_Game
        a list of objects containing all NSO games available under NSO's emulation softwares
        """
        return [ Classic_Game(**iterable) for iterable in self._get('/api/v1/classic_games',
            query = {
                'statuses[]': statuses,
                'country': country,
            }
        ).json() ]

    def getV1GiftCategories(self, country:str) -> list:
        """GET - Gets the current icon rewards available

        Parameters
        ----------
        country : str
        the account's country code

        Returns
        -------
        list
            Gift_Category
        a list of Gift_Category objects
        """
        return [ Gift_Category(**iterable) for iterable in self._get('/api/v1/gift_categories',
            query = {
                'country': country,
            }
        ).json() ]

    def getV2PickupItems(self, country:str) -> dict:
        """
        Unfinished
        """
        return [ Pickup_Item(**iterable) for iterable in self._get('/api/v2/pickup_items',
            query = {
                'country': country,
            }
        ).json() ]
