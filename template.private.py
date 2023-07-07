headers:dict = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '[REDACTED]',
    'Host': 'accounts.nintendo.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519', # Doesn't really matter
}

## 'Cookie' may include the following cookies:
# NASID -- a JWT formatted like the below:
# Header:
# {
#  "alg": "HS256"
# }
#
# Payload:
# {
#  "iss": "https://accounts.nintendo.com", -- the issuer
#  "jti": integer, -- the token identifier
#  "_ext": {
#    "u": integer
#  },
#  "exp": integer, -- UNIX timestamp for expiry -- 730 days after issue date
#  "iat": integer, -- UNIX timestamp for issuing date
#  "sub": "string", -- this is your Nintendo Account ID
#  "typ": "session" -- this is the type of the token
# }
