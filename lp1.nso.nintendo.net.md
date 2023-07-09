# nso-applet-api

Prepend all routes with https://lp1.nso.nintendo.net.  
All requests are made with HTTP2.

| Name | Implements | Method |
| --- | --- | --- |
| [NSOAppletAPI.getUserInfo()](#getuserinfo) | [/api/v1/user/profile](https://lp1.nso.nintendo.net/api/v1/user/profile) | **GET** |
| [NSOAppletAPI.getV1Cookies()](#getv1cookies) | [/api/v1/cookies](https://lp1.nso.nintendo.net/api/v1/cookies) | **GET** |
| [NSOAppletAPI.v1PostLogin()](#v1postlogin) | [/api/v1/login](https://lp1.nso.nintendo.net/api/v1/login) | **POST** |
| [NSOAppletAPI.getV1LClassicsTitles()](#getv1lclassicstitles) | [/api/v1/classic_games](https://lp1.nso.nintendo.net/api/v1/classic_games) | **GET** |
| [NSOAppletAPI.getV1GiftCategories()](#getv1giftcategories) | [/api/v1/gift_categories](https://lp1.nso.nintendo.net/api/v1/gift_categories) | **GET** |

## getUserInfo
Grabs your account's basic user information. Not a full response of data; just what appears to be necessary for the NSO Applet's purposes.

### Request

| Parameter | Type | Description |
| --- | --- | --- |
| country | str | the account's country code |

### Response

| Type | Description |
| --- | --- |
| [User_Info](#user_info) | an object with your returned user information |

## getV1Cookies
Stores the following cookies: `CloudFront-Key-Pair-Id`, `CloudFront-Policy`, `CloudFront-Signature`.  
They are returned in the `Set-Cookie` header of the response. `NSOAppletAPI.getV1Cookies()` only returns a [Cookie](#cookie) object.

### Request

| Parameter | Type | Description |
| --- | --- | --- |
| country | str | the account's country code |

### Response

| Type | Description |
| --- | --- |
| [Cookie](#cookie) | an object that contains the expiry information |

## v1PostLogin
Posts a login and receives a [Login](#login) object with point-related data.

### Request

| Parameter | Type | Description |
| --- | --- | --- |
| country | str | the account's country code |

### Response

| Type | Description |
| --- | --- |
| [Login](#login) | an object that contains your [Point_Wallet](#point_wallet) |

## getV1LClassicsTitles
Gets the current titles available under NSO's emulation softwares.

### Request

| Parameter | Type | Description |
| --- | --- | --- |
| statuses | str | correlates to statuses[] - commonly is `published` |
| country | str | the account's country code |

### Response

| Type | Description |
| --- | --- |
| list<[Classic_Game](#classic_game)> | a list of objects containing all NSO games available under NSO's emulation softwares |

## getV1GiftCategories
Returns the current [Gift Categories](#gift_category) that are available.

### Request

| Parameter | Type | Description |
| --- | --- | --- |
| country | str | the account's country code |

### Response

| Type | Description |
| --- | --- |
| list<[Gift_Category](#gift_category)> | a list of objects containing gift category information |

# Objects

| Name | Origin |
| --- | --- |
| [User_Info](#user_info) | [nso](/nso/structures.py) |
| [Cookie](#cookie) | [nso](/nso/structures.py) |
| [Login](#login) | [nso](/nso/structures.py) |
| [Point_Wallet](#point_wallet) | [nso](/nso/structures.py) |
| [Total_Point](#total_point) | [nso](/nso/structures.py) |
| [Expiration](#expiration) | [nso](/nso/structures.py) |
| [Point](#point) | [nso](/nso/structures.py) |
| [Classic_Game](#classic_game) | [nso](/nso/structures.py) |
| [Bundled_Region](#bundled_region) | [nso](/nso/structures.py) |
| [Gift_Category](#gift_category) | [nso](/nso/structures.py) |
| [Rating_Info](#rating_info) | [nso](/nso/structures.py) |
| [Rating_System](#rating_system) | [nso](/nso/structures.py) |
| [Rating](#rating) | [nso](/nso/structures.py) |
| [Content_Descriptor](#content_descriptor) | [nso](/nso/structures.py) |
| [Gift](#gift) | [nso](/nso/structures.py) |
| [Reward](#reward) | [nso](/nso/structures.py) |
| [Reward_Status](#reward_status) | [nso](/nso/structures.py) |

## User_Info

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | str | Your Nintendo Account ID |
| country | str | Your account's country code |
| birthday | str | Your account's birthday |
| banned | bool | Whether your account is banned or not |
| analytics_opted_in | bool | If you're opted in to submitting analytical data |
| is_region_quebec | bool | Whether your account is from Quebec -- required because of specific laws regarding rewards systems, I believe |

## Cookie

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| expires | int | UNIX timestamp with cookie expiry date |

## Login

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| received_points | list | A list with your received points -- I've only ever seen this empty |
| point_wallet | [Point_Wallet](#point_wallet) | A list of your current points, as well as expirations |

## Point_Wallet

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| total_point | [Total_Point](#total_point) | This object includes your total amount of platinum points |
| expirations | list<[Expiration](#expiration)> | Your points alongside their expiration dates |

## Total_Point

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| platinum | int | Your total number of platinum points |

## Expiration

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| expires_at | str | A date of when the points will expire |
| point | [Point](#point) | The points that will expire |

## Point

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| platinum | int | Total number of platinum points for a context |

## Classic_Game

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| status | str | Seems to always be `publishing` |
| title_id | str | Title IDs for respective console |
| title_name | str | Name of the game |
| application_id | str | Matches an NSO console emulator title ID |
| application_type | str | Console type description |
| bundled_region | [Bundled_Region](#bundled_region) | Includes special region information. Commonly, this is `None` |
| icon_url | str | Game's icon URL |
| publisher | str | Game's publisher |
| is_unknown_release_date | bool | Whether the release date is known or not |
| released_at | str | When game was initially released |
| published_at | str | When game was added to NSO |

## Bundled_Region

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| region | str | Region code (i.e. `EUR`, `KR`, etc) |
| languages | list | List of language codes. Can be `None` |

## Gift_Category

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | str | The category ID |
| key | str | The category's key |
| name | str | The category's name |
| image_url | str | The category's image icon URL |
| description | str | The category's description info (often updated) |
| required_membership_type | str | The membership type required to access the category for rewards. Often `'membership'` |
| supported_tags | list<str> | The supported tags by the category (`['character', 'background', 'frame']`) |
| key_color | str | The HEX color code for the category's theme color |
| rating_info | [Rating_Info](#rating_info) | The rating information |
| gifts | list<[Gift](#gift)> | The gifts obtainable from this category |

## Rating_Info

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| nsuid | int | The nsuId of the game |
| rating_system | [Rating_System](#rating_system) | The Rating System information -- i.e. US is ESRB |
| rating | [Rating](#rating) | The Rating information |
| content_descriptors | list<[Content_Descriptor](#content_descriptor)> | The Content Descriptor |

## Rating_System

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | int | Rating ID |
| name | [Rating_System](#rating_system) | Rater name -- i.e. `'ESRB'` |

## Rating

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | int | The rating ID |
| name | str | The rating type (`'E'`, `'E10+'`, etc) |
| age | int | The starting age |
| provisional | bool | Unfinished, temporary rating |
| image_url | str | Rating image URL |

## Content_Descriptor

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | int | The content descriptor ID |
| name | str | The descriptor name (i.e. `'Comic Mischief'`) |
| type | str | Typically `'descriptor'` |
| image_url | str | Is an image URL. Usually `None` |

## Gift

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | str | ID of Gift. Normally [`Gift_Category.key`](#gift_category)`_%4d` |
| name | str | Name of Gift. Can be `None` |
| tags | list<str> | Type of gift. One of [`Gift_Category.supported_tags`](#gift_category) |
| meta | str | Can be `None`. Usually reserved for Animal Crossing characters with stringified JSON birthdays |
| created_at | str | Gift creation date |
| updated_at | str | Gift update date |
| reward | [Reward](#reward) | Reward object |

## Reward

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| id | str | ID of Reward |
| thumbnail_url | str | Reward image URL |
| point | [Point](#point) | Points for purchase |
| begins_at | str | Time of Reward release date |
| ends_at | str | Time of Reward expiry date |
| reward_status | [Reward_Status](#reward_status) | Reward Status |

## Reward_Status

An object with the following:

| Name | Type | Description |
| --- | --- | --- |
| user_id | str | The accessor's user ID |
| limited | bool | If the item is limited(?) |

# Testing the NSO Webapplet with dev tools

<details>
  <summary><b>Show basic tutorial</b></summary

  Some quick documentation on getting the NSO webapplet in your browser (from information discovered by Samuel Elliot):
  ```
  https://accounts.nintendo.com/connect/1.0.0/authorize?client_id=f4e5f2f3e022208b&response_type=id_token&scope=openid&redirect_uri=nintendo://lhub.nx.sys&state=a
  ```
  Get id_token from the above.

  Go to <https://lp1.nso.nintendo.net> -- set your user agent to something like `Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519`

  Add breakpoints to the index's script at `var n = navigator.userAgent.includes("NintendoBrowser");` and the static/js/main.1d72eb58.js at `setNaAuthTokenAvailableCallback: function(e) {e(void 0, void 0, EP.b)},`

  Reload page and, on first breakpoint, paste the below
  ```
  Object.defineProperty(navigator, 'userAgent', {get: () => 'no'})
  ```
  Then resume and on second breakpoint, paste the below, replacing "id_token" with your id_token from before
  ```
  e(undefined, undefined, 'id_token')
  ```

  If you'd like a bunch of info dump, make a breakpoint anywhere with `r.getState()`, then run `r.getState();` in the Console whenever it breaks there.

</details>
