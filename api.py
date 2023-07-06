# Made by Deltaion Lee (MCMi460) on Github
import os, httpx, json, requests
from private import headers # Necessary for API requests
# See template.private.py for more information regarding the private.py

os.system('')
class Color:
    DEFAULT = '\033[0m'
    RED = '\033[91m'
    PURPLE = '\033[0;35m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'

class API_Exception(Exception):
    def __init__(self, message, data = '') -> None:
        self.log(data, 'API_Exception: ' + message)
        super().__init__(message)

    def log(self, *text:str) -> None:
        print(Color.RED + 'Custom traceback:\n' + Color.YELLOW + '\n'.join(map(str, text)) + Color.DEFAULT)

class API:
    def __init__(self) -> None:
        X_Api_Token = self.authorize() # Set X_Api_Token

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
            raise API_Exception(cookies['message'], data = cookies)

    def authorize(self):
        auth = requests.get(
            'https://accounts.nintendo.com/connect/1.0.0/authorize?client_id=f4e5f2f3e022208b&response_type=id_token&scope=openid&redirect_uri=nintendo://lhub.nx.sys&state=a',
            headers = headers,
            allow_redirects = False
        ) # Simulate logging in. Steal the request headers from an actual request to the same URL.
        # See template.private.py for more information regarding the private.py

        data = auth.headers['location'].replace('nintendo://lhub.nx.sys#id_token=', '').split('&')

        return data[0]

    def _formatQueryString(self, route:str, query:dict) -> str:
        return route + '?' + '&'.join( '%s=%s' % (key, query[key]) for key in query.keys() )

    def get(self, route:str, *, query:dict = {}) -> httpx.Response:
        if query:
            route = self._formatQueryString(route, query)

        print('[GET] ' + route)

        result = self.Session.get(self.host + route)
        print('[GET] ' + route + ' <Response Code [%s]>' % result.status_code)
        return result

    def post(self, route:str, *, query:dict = {}) -> httpx.Response:
        if query:
            route = self._formatQueryString(route, query)

        print('[POST] ' + route)

        result = self.Session.post(self.host + route)
        print('[POST] ' + route + ' <Response Code [%s]>' % result.status_code)
        return result

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
        return self.get('/api/v1/user/profile',
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
        return self.get('/api/v1/cookies',
            query = {
                'country': country,
            }
        ).json()

    def v1PostLogin(self, country:str):
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
        return self.post('/api/v1/login',
            query = {
                'country': country,
            }
        ).json()

    def getV1LClassicsTitles(self, statuses:str, country:str):
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
        a list of dictionaries containing all NSO games available under NSO's emulation softwares
            dict
                Keys:
                    status : str
                    title_id : str
                    title_name : str
                    application_id : str
                    application_type : str
                    bundled_region : None || dict
                        Keys:
                            region : str
                            languages : None || list
                    icon_url : str
                    publisher : str
                    is_unknown_release_date : bool
                    released_at : str
                    published_at : str
        """
        return self.get('/api/v1/classic_games',
            query = {
                'statuses[]': statuses,
                'country': country,
            }
        ).json()

    def getV1GiftCategories(self, country:str):
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
        a list of dictionaries for individual collections currently available
            dict
                Keys:
                    id : str
                    key : str
                    name : str
                    image_url : str
                    description : str
                    required_membership_type : str
                    # 'membership'
                    supported_tags : list
                        str
                        # 'character'/'background'/'frame'
                    key_color : str
                    rating_info : dict
                        Keys:
                            nsuid : int
                            rating_system : dict
                                Keys:
                                    id : int
                                    name : str
                            rating : dict
                                Keys
                                    id : int
                                    name : str
                                    age : int
                                    provisional : bool
                                    image_url : str
                            content_descriptors : list
                                dict
                                    id : int
                                    name : str
                                    type : str
                                    image_url : None || str
                    gifts : list
                        dict
                            id : str
                            name : str
                            tags : list
                                str
                                # 'character'/'background'/'frame'
                            meta : None || dict
                            # This one is really variable
                            # Animal Crossing characters seem to have birthdays
                                Keys:
                                    birthday : str
                            created_at : str
                            updated_at : str
                            reward : dict
                                Keys:
                                    id : str
                                    thumbnail_url : str
                                    point : dict
                                        Keys:
                                            platinum : int
                                    begins_at : str
                                    ends_at : str
                                    reward_status : dict
                                        Keys:
                                            user_id : str
                                            limited : bool
        """
        return self.get('/api/v1/gift_categories',
            query = {
                'country': country,
            }
        ).json()

    def getV2PickupItems(self, country:str):
        """
        Unfinished
        """
        return self.get('/api/v2/pickup_items',
            query = {
                'country': country,
            }
        ).json()
