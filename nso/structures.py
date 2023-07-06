# Made by Deltaion Lee (MCMi460) on Github
from . import *

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
    def __init__(self, **kwargs) -> None:
        self.status:str = kwargs.get('status')
        self.title_id:str = kwargs.get('title_id')
        self.title_name:str = kwargs.get('title_name')
        self.application_id:str = kwargs.get('application_id')
        self.application_type:str = kwargs.get('application_type')
        self.bundled_region:dict = kwargs.get('bundled_region')
        self.icon_url:str = kwargs.get('icon_url')
        self.publisher:str = kwargs.get('publisher')
        self.is_unknown_release_date:bool = kwargs.get('is_unknown_release_date')
        self.released_at:str = kwargs.get('released_at')
        self.published_at:str = kwargs.get('published_at')

    def __str__(self) -> str:
        return toString(self)

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
        self.gifts:typing.List[Gift] = [ Gift(**iterable) for iterable in kwargs.get('gifts') ]

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
        self.content_descriptors:typing.List[Content_Descriptor] = [ Content_Descriptor(**iterable) for iterable in kwargs.get('content_descriptors') ]

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
    iterable : dict
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
    iterable : dict
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
