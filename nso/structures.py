# Made by Deltaion Lee (MCMi460) on Github
from . import *

##############################
# NSOAppletAPI.getUserInfo() #
##############################
class User_Info:
    """
    response : dict
        Keys:
            id : str
            country : str
            birthday : str
            banned : bool
            analytics_opted_in : bool
            is_region_quebec : bool
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.country:str = kwargs.get('country')
        self.birthday:str = kwargs.get('birthday')
        self.banned:bool = kwargs.get('banned')
        self.analytics_opted_in:bool = kwargs.get('analytics_opted_in')
        self.is_region_quebec:bool = kwargs.get('is_region_quebec')

    def __str__(self) -> str:
        return toString(self)

###############################
# NSOAppletAPI.getV1Cookies() #
###############################
class Cookie:
    """
    response : dict
        Keys:
            expires : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.expires:int = kwargs.get('expires')

    def __str__(self) -> str:
        return toString(self)

##############################
# NSOAppletAPI.v1PostLogin() #
##############################
class Login:
    """
    response : dict
        Keys:
            received_points : list
            # I've only ever seen this empty
            point_wallet : Point_Wallet
    """
    def __init__(self, **kwargs:dict) -> None:
        self.received_points:list = kwargs.get('received_points')
        self.point_wallet:Point_Wallet = Point_Wallet() if kwargs.get('point_wallet', {}) is None else Point_Wallet(**kwargs.get('point_wallet', {}))

    def __str__(self) -> str:
        return toString(self)

class Point_Wallet:
    """
    point_wallet : dict
        Keys:
            total_point : Total_Point
            expirations : list
                Expiration
    """
    def __init__(self, **kwargs:dict) -> None:
        self.total_point:Total_Point = Total_Point() if kwargs.get('total_point', {}) is None else Total_Point(**kwargs.get('total_point', {}))
        self.expirations:typing.List[Expiration] = [ Expiration(**iterable) for iterable in kwargs.get('expirations', []) ]

    def __str__(self) -> str:
        return toString(self)

class Total_Point:
    """
    total_point : dict
        Keys:
            platinum : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.platinum:int = kwargs.get('platinum')

    def __str__(self) -> str:
        return toString(self)

class Expiration:
    """
    iterable : dict
        Keys:
            expires_at : str
            point : Point
    """
    def __init__(self, **kwargs:dict) -> None:
        self.expires_at:str = kwargs.get('expires_at')
        self.point:Point = Point() if kwargs.get('point', {}) is None else Point(**kwargs.get('point', {}))

    def __str__(self) -> str:
        return toString(self)

class Point:
    """
    point : dict
        Keys:
            platinum : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.platinum:int = kwargs.get('platinum')

    def __str__(self) -> str:
        return toString(self)

#######################################
# NSOAppletAPI.getV1LClassicsTitles() #
#######################################
class Classic_Game:
    """
    iterable : dict
        Keys:
            status : str
            title_id : str
            title_name : str
            application_id : str
            application_type : str
            bundled_region : None || Bundled_Region
            icon_url : str
            publisher : str
            is_unknown_release_date : bool
            released_at : str
            published_at : str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.status:str = kwargs.get('status')
        self.title_id:str = kwargs.get('title_id')
        self.title_name:str = kwargs.get('title_name')
        self.application_id:str = kwargs.get('application_id')
        self.application_type:str = kwargs.get('application_type')
        self.bundled_region:Bundled_Region = Bundled_Region(**kwargs.get('bundled_region')) if kwargs.get('bundled_region') else None
        self.icon_url:str = kwargs.get('icon_url')
        self.publisher:str = kwargs.get('publisher')
        self.is_unknown_release_date:bool = kwargs.get('is_unknown_release_date')
        self.released_at:str = kwargs.get('released_at')
        self.published_at:str = kwargs.get('published_at')

    def __str__(self) -> str:
        return toString(self)

class Bundled_Region:
    """
    bundled_region : dict
        Keys:
            region : str
            languages : None || list
    """
    def __init__(self, **kwargs:dict) -> None:
        self.region:str = kwargs.get('region')
        self.languages:list = kwargs.get('languages')

######################################
# NSOAppletAPI.getV1GiftCategories() #
######################################
class Gift_Category:
    """
    iterable : dict
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
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.key:str = kwargs.get('key')
        self.name:str = kwargs.get('name')
        self.image_url:str = kwargs.get('image_url')
        self.description:str = kwargs.get('description')
        self.required_membership_type:str = kwargs.get('required_membership_type')
        self.supported_tags:typing.List[str] = kwargs.get('supported_tags')
        self.key_color:str = kwargs.get('key_color')
        self.rating_info:Rating_Info = Rating_Info() if kwargs.get('rating_info', {}) is None else Rating_Info(**kwargs.get('rating_info', {}))
        self.gifts:typing.List[Gift] = [ Gift(**iterable) for iterable in kwargs.get('gifts', []) ]

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
    def __init__(self, **kwargs:dict) -> None:
        self.nsuid:int = kwargs.get('nsuid')
        self.rating_system:Rating_System = Rating_System() if kwargs.get('rating_system', {}) is None else Rating_System(**kwargs.get('rating_system', {}))
        self.rating:Rating = Rating() if kwargs.get('rating', {}) is None else Rating(**kwargs.get('rating', {}))
        self.content_descriptors:typing.List[Content_Descriptor] = [ Content_Descriptor(**iterable) for iterable in kwargs.get('content_descriptors', []) ]

    def __str__(self) -> str:
        return toString(self)

class Rating_System:
    """
    rating_system : dict
        Keys:
            id : int
            name : str
    """
    def __init__(self, **kwargs:dict) -> None:
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
    def __init__(self, **kwargs:dict) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.age:int = kwargs.get('age')
        self.provisional:bool = kwargs.get('provisional')
        self.image_url:str = kwargs.get('image_url')

    def __str__(self) -> str:
        return toString(self)

class Content_Descriptor:
    """
    iterable : dict
        Keys:
            id : int
            name : str
            type : str
            image_url : None || str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.type:str = kwargs.get('type')
        self.image_url:str = kwargs.get('image_url')

    def __str__(self) -> str:
        return toString(self)

class Gift:
    """
    iterable : dict
        Keys:
            id : str
            name : None || str
            tags : list
                str
                # 'character'/'background'/'frame'
            meta : None || str
            # This one is really variable
            # Animal Crossing characters seem to have birthdays
            # And the string is just stringified JSON
            # Such as "meta": "{\"birthday\":\"07-02\"}"
            created_at : str
            updated_at : str
            reward : Reward
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.name:str = kwargs.get('name')
        self.tags:typing.List[str] = kwargs.get('tags')
        self.meta:str = kwargs.get('meta')
        self.created_at:str = kwargs.get('created_at')
        self.updated_at:str = kwargs.get('updated_at')
        self.reward:Reward = Reward() if kwargs.get('reward', {}) is None else Reward(**kwargs.get('reward', {}))

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
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.thumbnail_url:str = kwargs.get('thumbnail_url')
        self.point:Point = Point() if kwargs.get('point', {}) is None else Point(**kwargs.get('point', {}))
        self.begins_at:str = kwargs.get('begins_at')
        self.ends_at:str = kwargs.get('ends_at')
        self.reward_status:Reward_Status = Reward_Status() if kwargs.get('reward_status', {}) is None else Reward_Status(**kwargs.get('reward_status', {}))

    def __str__(self) -> str:
        return toString(self)

class Reward_Status:
    """
    reward_status : dict
        Keys:
            user_id : str
            limited : bool
    """
    def __init__(self, **kwargs:dict) -> None:
        self.user_id:str = kwargs.get('user_id')
        self.limited:bool = kwargs.get('limited')

    def __str__(self) -> str:
        return toString(self)

###################################
# NSOAppletAPI.getV2PickupItems() #
###################################
class Pickup_Item:
    """
    response : dict
        Keys:
            id : str
            status : str
            countries : list
                str
            condition_subscription_type : None || str
            priority : str
            template : str
            products : list
                product
            published_at : str
            expired_at : str
            display_meta : str
            distribution : Distribution
            rating_info : Rating_Info
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.status:str = kwargs.get('status')
        self.countries:typing.List[str] = kwargs.get('countries')
        self.condition_subscription_type:str = kwargs.get('condition_subscription_type')
        self.priority:str = kwargs.get('priority')
        self.template:str = kwargs.get('template')
        self.products:typing.List[Product] = [ Product(**iterable) for iterable in kwargs.get('products', []) ]
        self.published_at:str = kwargs.get('published_at')
        self.expired_at:str = kwargs.get('expired_at')
        self.display_meta:str = kwargs.get('display_meta')
        self.distribution:Distribution = Distribution() if kwargs.get('distribution', {}) is None else Distribution(**kwargs.get('distribution', {}))
        self.rating_info:Rating_Info = Rating_Info() if kwargs.get('rating_info', {}) is None else Rating_Info(**kwargs.get('rating_info', {}))

    def __str__(self) -> str:
        return toString(self)

class Product:
    """
    iterable : dict
        Keys:
            nsuid : int
            application_id : str
            title_name : str
            icon_url : str
            icon_sizes : list
                int
            classic_title_id : None || str
            classic_title_icon_url : None || str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.nsuid:int = kwargs.get('nsuid')
        self.application_id:str = kwargs.get('application_id')
        self.title_name:str = kwargs.get('title_name')
        self.icon_url:str = kwargs.get('icon_url')
        self.icon_sizes:typing.List[int] = kwargs.get('icon_sizes')
        self.classic_title_id:str = kwargs.get('classic_title_id')
        self.classic_title_icon_url:str = kwargs.get('classic_title_icon_url')

    def __str__(self) -> str:
        return toString(self)

class Distribution:
    """
    iterable : dict
        Keys:
            language : str
            thumbnail_url : str
            cover_image_url : str
            cover_video_url : str
            button : Button
            content : None || str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.language:str = kwargs.get('language')
        self.thumbnail_url:str = kwargs.get('thumbnail_url')
        self.cover_image_url:str = kwargs.get('cover_image_url')
        self.cover_video_url:str = kwargs.get('cover_video_url')
        self.button:Button = Button() if kwargs.get('button', {}) is None else Button(**kwargs.get('button', {}))
        self.content:str = kwargs.get('content')

    def __str__(self) -> str:
        return toString(self)

class Button:
    """
    iterable : dict
        Keys:
            text : str
            url : str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.text:str = kwargs.get('text')
        self.url:str = kwargs.get('url')

    def __str__(self) -> str:
        return toString(self)
