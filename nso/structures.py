# Made by Deltaion Lee (MCMi460) on Github
from . import *

###################
# Data Structures #
###################
class Data:
    def __str__(self) -> str:
        return toString(self)
    
    def fixNone(self, type, name:str, kwargs:dict):
        return type() if kwargs.get(name, {}) is None else type(**kwargs.get(name, {}))

##############################
# NSOAppletAPI.getUserInfo() #
##############################
class User_Info(Data):
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

###############################
# NSOAppletAPI.getV1Cookies() #
###############################
class Cookie(Data):
    """
    response : dict
        Keys:
            expires : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.expires:int = kwargs.get('expires')

##############################
# NSOAppletAPI.v1PostLogin() #
##############################
class Login(Data):
    """
    response : dict
        Keys:
            received_points : list
            # I've only ever seen this empty
            point_wallet : Point_Wallet
    """
    def __init__(self, **kwargs:dict) -> None:
        self.received_points:list = kwargs.get('received_points')
        self.point_wallet:Point_Wallet = self.fixNone(Point_Wallet, 'point_wallet', kwargs)

class Point_Wallet(Data):
    """
    point_wallet : dict
        Keys:
            total_point : Total_Point
            expirations : list
                Expiration
    """
    def __init__(self, **kwargs:dict) -> None:
        self.total_point:Total_Point = self.fixNone(Total_Point, 'total_point', kwargs)
        self.expirations:typing.List[Expiration] = [ Expiration(**iterable) for iterable in kwargs.get('expirations', []) ]

class Total_Point(Data):
    """
    total_point : dict
        Keys:
            platinum : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.platinum:int = kwargs.get('platinum')

class Expiration(Data):
    """
    iterable : dict
        Keys:
            expires_at : str
            point : Point
    """
    def __init__(self, **kwargs:dict) -> None:
        self.expires_at:str = kwargs.get('expires_at')
        self.point:Point = self.fixNone(Point, 'point', kwargs)

class Point(Data):
    """
    point : dict
        Keys:
            platinum : int
    """
    def __init__(self, **kwargs:dict) -> None:
        self.platinum:int = kwargs.get('platinum')

#######################################
# NSOAppletAPI.getV1LClassicsTitles() #
#######################################
class Classic_Game(Data):
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

class Bundled_Region(Data):
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
class Gift_Category(Data):
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
        self.rating_info:Rating_Info = self.fixNone(Rating_Info, 'rating_info', kwargs)
        self.gifts:typing.List[Gift] = [ Gift(**iterable) for iterable in kwargs.get('gifts', []) ]

class Rating_Info(Data):
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
        self.rating_system:Rating_System = self.fixNone(Rating_System, 'rating_system', kwargs)
        self.rating:Rating = self.fixNone(Rating, 'rating', kwargs)
        self.content_descriptors:typing.List[Content_Descriptor] = [ Content_Descriptor(**iterable) for iterable in kwargs.get('content_descriptors', []) ]

class Rating_System(Data):
    """
    rating_system : dict
        Keys:
            id : int
            name : str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:int = kwargs.get('id')
        self.name:str = kwargs.get('name')

class Rating(Data):
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

class Content_Descriptor(Data):
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

class Gift(Data):
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
        self.reward:Reward = self.fixNone(Reward, 'reward', kwargs)

class Reward(Data):
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
        self.reward_status:Reward_Status = self.fixNone(Reward_Status, 'reward_status', kwargs)

class Reward_Status(Data):
    """
    reward_status : dict
        Keys:
            user_id : str
            limited : bool
    """
    def __init__(self, **kwargs:dict) -> None:
        self.user_id:str = kwargs.get('user_id')
        self.limited:bool = kwargs.get('limited')

###################################
# NSOAppletAPI.getV2PickupItems() #
###################################
class Pickup_Item(Data):
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
        self.distribution:Distribution = self.fixNone(Distribution, 'distribution', kwargs)
        self.rating_info:Rating_Info = self.fixNone(Rating_Info, 'rating_info', kwargs)

class Product(Data):
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

class Distribution(Data):
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
        self.button:Button = self.fixNone(Button, 'button', kwargs)
        self.content:str = kwargs.get('content')

class Button(Data):
    """
    iterable : dict
        Keys:
            text : str
            url : str
    """
    def __init__(self, **kwargs:dict) -> None:
        self.text:str = kwargs.get('text')
        self.url:str = kwargs.get('url')

#################################
# NSOAppletAPI.getV1UserRightCategories() #
#################################
class Right_Category(Data):
    """
    iterable : dict
        Keys:
            id : str
            key : str
            name : str
            image_url : str
            supported_tags : list
                str
                # 'character'/'background'/'frame'
            rights : list
                Right
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.key:str = kwargs.get('key')
        self.name:str = kwargs.get('name')
        self.image_url:str = kwargs.get('image_url')
        self.supported_tags:typing.List[str] = kwargs.get('supported_tags')
        self.rights:typing.List[Right] = [ Right(**iterable) for iterable in kwargs.get('rights', []) ]

class Right(Data):
    """
    iterable : dict
        Keys:
            id : str
            user_id : str
            content_url : str
            created_at : str
            updated_at : str
            gift : Gift # gift.reward will always be empty
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.user_id:str = kwargs.get('user_id')
        self.content_url:str = kwargs.get('content_url')
        self.created_at:str = kwargs.get('created_at')
        self.updated_at:str = kwargs.get('updated_at')
        self.gift:Gift = self.fixNone(Gift, 'gift', kwargs)

#################################
# NSOAppletAPI.getV1UserIcons() #
#     UNFINISHED CURRENTLY      #
#################################
class User_Icon(Data):
    """
    iterable : dict
        Keys:
            id : str
            updated_at : str
            character : Character
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.updated_at:str = kwargs.get('updated_at')
        self.character:Character = self.fixNone(Character, 'character', kwargs)

class Character(Data):
    """
    iterable : dict
        Keys:
            shadow : str
            image_right : Image_Right
    """
    def __init__(self, **kwargs:dict) -> None:
        self.shadow:str = kwargs.get('shadow')
        self.image_right:Image_Right = self.fixNone(Image_Right, 'image_right', kwargs)

class Image_Right(Data):
    """
    iterable : dict
        Keys:
            id : str
            user_id : str
            content_url : str
            created_at : str
            updated_at : str
            gift : Gift
    """
    def __init__(self, **kwargs:dict) -> None:
        self.id:str = kwargs.get('id')
        self.user_id:str = kwargs.get('user_id')
        self.content_url:str = kwargs.get('content_url')
        self.created_at:str = kwargs.get('created_at')
        self.updated_at:str = kwargs.get('updated_at')
        self.gift:Gift = self.fixNone(Gift, 'gift', kwargs)
