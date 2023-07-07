# Made by Deltaion Lee (MCMi460) on Github
from . import *

class NSOAppletAPI:
    def __init__(self, *, headers:dict = None) -> None:
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

        cookies = self.getV1Cookies('US') # Set cookies for the future
        self.expiry = cookies.get('expires', None)
        if not self.expiry:
            raise NSOAppletAPI_Exception(cookies['message'], data = cookies)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def _log(self, *text:str) -> None:
        print(Color.WHITE + ' '.join(map(str, text)) + Color.DEFAULT)

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

        data = auth.headers['location'].replace('nintendo://lhub.nx.sys#id_token=', '').split('&')

        return data[0]

    ### API ROUTES ###
    ## Disclaimer:
    ## I do not necessarily have all of the information regarding these endpoints
    ## If you get a return value that differs from mine on one of these,
    ## please make a new issue to tell me!
    ## Thanks! - MCMi460
    ## Note:
    ## I will also note beside endpoints that require an NSO membership
    ## in order to operate.
    def getUserInfo(self, country:str) -> dict:
        """GET - Gets the user's info

        Parameters
        ----------
        country : str
        The account's country code

        Returns
        -------
        dict
        a dictionary of the user's info
            Keys:
                id : str
                country : str
                birthday : str
                banned : bool
                analytics_opted_in : bool
                is_region_quebec : bool
        """
        return self._get('/api/v1/user/profile',
            query = {
                'country': country,
            }
        ).json()

    def getV1Cookies(self, country:str) -> dict:
        """GET - Stores the following cookies: CloudFront-Key-Pair-Id, CloudFront-Policy, CloudFront-Signature

        Parameters
        ----------
        country : str
        The account's country code

        Returns
        -------
        dict
        a dictionary that contains the expiry information
            Keys:
                expires : int
        """
        return self._get('/api/v1/cookies',
            query = {
                'country': country,
            }
        ).json()

    def v1PostLogin(self, country:str) -> dict:
        """POST - Posts a login

        Parameters
        ----------
        country : str
        The account's country code

        Returns
        -------
        dict
        a dictionary that contains information regarding the user's My Nintendo point balance
            Keys:
                received_points : list
                point_wallet : dict
                    Keys:
                        total_point : dict
                            Keys:
                                platinum : int
                        expirations : list
        """
        return self._post('/api/v1/login',
            query = {
                'country': country,
            }
        ).json()

    def getV1LClassicsTitles(self, statuses:str, country:str) -> dict:
        """GET - Gets the current titles available under NSO's emulation softwares

        Parameters
        ----------
        statuses : str
        Correlates to statuses[] - defaults to 'published'
        country : str
        The account's country code

        Returns
        -------
        list
            Classic_Game
        a list of dictionaries containing all NSO games available under NSO's emulation softwares
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
        statuses : str
        Correlates to statuses[] - defaults to 'published'
        country : str
        The account's country code

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
        return self._get('/api/v2/pickup_items',
            query = {
                'country': country,
            }
        ).json()
