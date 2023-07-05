## Testing the NSO Webapplet with dev tools

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

</details>

# NSOApplet

All requests are over HTTP2.  
For shorthand, please prepend `https://lp1.nso.nintendo.net/api`.  
`%s` refers to a redacted piece of information that the user will have to supply themself.

| Name | Method |
| --- | --- |
| [/v1/classic_games/](#getv1lclassicstitles) | **GET** |
| [/v1/cookies/](#getv1cookies) | **GET** |

## Standard Headers
*These tend to be in most of my requests*
| Key | Value |
| --- | --- |
| Accept | `application/json, text/plain, */*` |
| Accept-Encoding | `gzip, deflate, br` |
| Accept-Language | `en-US` |
| Cache-Control | `no-cache` |
| Cookie | `CloudFront-Key-Pair-Id=%s; CloudFront-Policy=%s; CloudFront-Signature=%s` |
| Pragma | `no-cache` |
| Referer | `https://lp1.nso.nintendo.net/%s` |
| Sec-Fetch-Dest | `empty` |
| Sec-Fetch-Mode | `cors` |
| Sec-Fetch-Site | `same-origin` |
| User-Agent | `Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519` |
| X-Api-Token | `%s` |

# getV1LClassicsTitles
## Route
`/v1/classic_games/`
## Request
### Headers
[Standard Request Headers](#standard-headers)
### Query String Parameters
*Default values taken from my requests*
| Key | Value |
| --- | --- |
| statuses[] | `publishing` |
| country | `US` |
## Response
### Headers
> Doesn't matter for now

### Content
Trimmed example response:
```json
[
    {
        "status": "publishing",
        "title_id": "CLV-P-NAAJE",
        "title_name": "EarthBound Beginnings",
        "application_id": "0100d870045b6000",
        "application_type": "nes",
        "bundled_region": null,
        "icon_url": "https://lp1.nso.nintendo.net/game_introduction/classic_game/icon/320/CLV-P-NAAJE.webp",
        "publisher": "Nintendo",
        "is_unknown_release_date": false,
        "released_at": "2015-06-14",
        "published_at": "2022-02-09T01:00:00.000Z"
    },
    {
        "status": "publishing",
        "title_id": "M-9155_e",
        "title_name": "Pulseman",
        "application_id": "0100b3c014bda000",
        "application_type": "md_e",
        "bundled_region": null,
        "icon_url": "https://lp1.nso.nintendo.net/game_introduction/classic_game/icon/476/M-9155_e.webp",
        "publisher": "SEGA",
        "is_unknown_release_date": false,
        "released_at": "2009-07-13",
        "published_at": "2023-04-19T01:00:00.000Z"
    },
    {
        "status": "publishing",
        "title_id": "A-8665_e",
        "title_name": "The Legend of Zelda™: The Minish Cap",
        "application_id": "010012f017576000",
        "application_type": "agb_e",
        "bundled_region": null,
        "icon_url": "https://lp1.nso.nintendo.net/game_introduction/classic_game/icon/448/A-8665_e.webp",
        "publisher": "Nintendo",
        "is_unknown_release_date": false,
        "released_at": "2005-01-10",
        "published_at": "2023-02-09T01:00:00.000Z"
    },
]
```

# getV1Cookies
## Route
`/v1/cookies/`
## Request
### Headers
[Standard Request Headers](#standard-headers)
### Query String Parameters
*Default values taken from my requests*
| Key | Value |
| --- | --- |
| country | `US` |
## Response
The cookies are set in the response headers, and the content returned includes a UNIX timestamp with the expiry date.
### Headers
Example headers:
| Key | Value |
| --- | --- |
| Content-Type | `application/json; charset=utf-8` |
| Date | `Wed, 05 Jul 2023 18:50:03 GMT` |
| Etag | `W/"%s"` |
| Referrer-Policy | `strict-origin-when-cross-origin` |
| Server | `nginx` |
| Set-Cookie | `CloudFront-Policy=%s; domain=lp1.nso.nintendo.net; path=/; HttpOnly; secure` |
| Set-Cookie | `CloudFront-Signature=%s; domain=lp1.nso.nintendo.net; path=/; HttpOnly; secure` |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains` |

### Content
Example response:
```json
{
  "expires": 1688593803
}
```
