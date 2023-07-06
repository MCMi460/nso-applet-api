# Made by Deltaion Lee (MCMi460) on Github
from . import *

class Gift_Category:
    """
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
            rating_info : Rating_Info
            gifts : list
                Gift
    """
    def __init__(self, **kwargs) -> None:
        self.id:str = kwargs.get('id')
        self.key:str = kwargs.get('key')
        self.name:str = kwargs.get('name')
        self.image_url:str = kwargs.get('image_url')
        self.description:str = kwargs.get('description')
        self.required_membership_type:str = kwargs.get('required_membership_type')
        self.supported_tags:typing.List[str] = kwargs.get('supported_tags')
        self.key_color:str = kwargs.get('key_color')
        self.rating_info:Rating_Info = Rating_Info(**kwargs.get('rating_info'))
        self.gifts:typing.List[Gift] = [ Gift(**gift) for gift in kwargs.get('gifts') ]

    def __str__(self) -> str:
        return toString(self)

class Rating_Info:
    """
    rating_info : dict
        Keys:
            nsuid : int
            rating_system : Rating_System
            rating : Rating
            content_descriptors : list
                Content_Descriptor
    """
    def __init__(self, **kwargs) -> None:
        self.nsuid:int = kwargs.get('nsuid')
        self.rating_system:Rating_System = Rating_System(**kwargs.get('rating_system'))
        self.rating:Rating = Rating(**kwargs.get('rating'))
        self.content_descriptors:typing.List[Content_Descriptor] = [ Content_Descriptor(**content_descriptor) for content_descriptor in kwargs.get('content_descriptors') ]

    def __str__(self) -> str:
        return toString(self)

class Rating_System:
    """
    rating_system : dict
        Keys:
            id : int
            name : str
    """
    def __init__(self, **kwargs) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')

    def __str__(self) -> str:
        return toString(self)

class Rating:
    """
    rating : dict
        Keys:
            id : int
            name : str
            age : int
            provisional : bool
            image_url : str
    """
    def __init__(self, **kwargs) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.age:int = kwargs.get('age')
        self.provisional:bool = kwargs.get('provisional')
        self.image_url:str = kwargs.get('image_url')

    def __str__(self) -> str:
        return toString(self)

class Content_Descriptor:
    """
    content_descriptor : dict
        Keys:
            id : int
            name : str
            type : str
            image_url : None || str
    """
    def __init__(self, **kwargs) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.type:str = kwargs.get('type')
        self.image_url:str = kwargs.get('image_url')

    def __str__(self) -> str:
        return toString(self)

class Gift:
    """
    gift : dict
        Keys:
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
            reward : Reward
    """
    def __init__(self, **kwargs) -> None:
        self.id:str = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.tags:typing.List[str] = kwargs.get('tags')
        self.meta:dict = kwargs.get('meta')
        self.created_at:str = kwargs.get('created_at')
        self.updated_at:str = kwargs.get('updated_at')
        self.reward:Reward = Reward(**kwargs.get('reward'))

    def __str__(self) -> str:
        return toString(self)

class Reward:
    """
    reward : dict
        Keys:
            id : str
            thumbnail_url : str
            point : Point
            begins_at : str
            ends_at : str
            reward_status : Reward_Status
    """
    def __init__(self, **kwargs) -> None:
        self.id:str = kwargs.get('id')
        self.thumbnail_url:str = kwargs.get('thumbnail_url')
        self.point:Point = Point(**kwargs.get('point'))
        self.begins_at:str = kwargs.get('begins_at')
        self.ends_at:str = kwargs.get('ends_at')
        self.reward_status:Reward_Status = Reward_Status(**kwargs.get('reward_status'))

    def __str__(self) -> str:
        return toString(self)

class Point:
    """
    point : dict
        Keys:
            platinum : int
    """
    def __init__(self, **kwargs) -> None:
        self.platinum:int = kwargs.get('platinum')

    def __str__(self) -> str:
        return toString(self)

class Reward_Status:
    """
    reward_status : dict
        Keys:
            user_id : str
            limited : bool
    """
    def __init__(self, **kwargs) -> None:
        self.user_id:str = kwargs.get('user_id')
        self.limited:bool = kwargs.get('limited')

    def __str__(self) -> str:
        return toString(self)

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

    def authorize(self, *, headers:dict = None) -> str:
        if not headers:
            raise NSOAppletAPI_Exception('missing authorization token generator headers')
        auth = requests.get(
            'https://accounts.nintendo.com/connect/1.0.0/authorize?client_id=f4e5f2f3e022208b&response_type=id_token&scope=openid&redirect_uri=nintendo://lhub.nx.sys&state=a',
            headers = headers,
            allow_redirects = False
        ) # Simulate logging in. Steal the request headers from an actual request to the same URL.
        # See template.private.py for more information regarding the private.py

        data = auth.headers['location'].replace('nintendo://lhub.nx.sys#id_token=', '').split('&')

        return data[0]

    def _log(self, *text:str) -> None:
        print(Color.WHITE + ' '.join(map(str, text)) + Color.DEFAULT)

    def _formatQueryString(self, route:str, query:dict) -> str:
        return route + '?' + '&'.join( '%s=%s' % (key, query[key]) for key in query.keys() )

    def _get(self, route:str, *, query:dict = {}) -> httpx.Response:
        if query:
            route = self._formatQueryString(route, query)

        self._log('[GET]', route)

        result = self.Session.get(self.host + route)
        self._log('[GET]', route, '<Response Code [%s]>' % result.status_code)
        return result

    def _post(self, route:str, *, query:dict = {}) -> httpx.Response:
        if query:
            route = self._formatQueryString(route, query)

        self._log('[POST]', route)

        result = self.Session.post(self.host + route)
        self._log('[POST]', route, '<Response Code [%s]>' % result.status_code)
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
        return self._get('/api/v1/classic_games',
            query = {
                'statuses[]': statuses,
                'country': country,
            }
        ).json()

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
        a list of Gift_Category objects
        """
        return [ Gift_Category(**gift_category) for gift_category in self._get('/api/v1/gift_categories',
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
