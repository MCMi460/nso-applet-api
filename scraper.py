# mega script by Deltaion Lee (MCMi460)
import os, re, httpx, json
from private import cloudFront_Key_Pair_Id, cloudFront_Policy, cloudFront_Signature

# headers, etc
url = 'https://lp1.nso.nintendo.net'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519',
    'accept-language': 'en-US,en;q=0.5',
}

cookies = {
    'CloudFront-Key-Pair-Id': cloudFront_Key_Pair_Id,
    'CloudFront-Policy': cloudFront_Policy,
    'CloudFront-Signature': cloudFront_Signature,
}

routes = [
    '/',
    '/static/js/vendors.af3d3c6f.js',
    '/static/css/main.321ba67a.css',
    '/static/js/main.1d72eb58.js',
]

# Enable/disable scripts
jsScrape = True
scrape = True
testAPI = True

# For API dissection
class Route:
    def __init__(self, *, route = '', name = '', method = ''):
        self.route = route
        self.name = name
        self.method = method

    def __str__(self):
        return '%s: %s \'%s\'' % (self.route if self.route else 'no route supplied', self.method if self.method else 'no method supplied', self.name if self.name else 'no name supplied')

class Gift:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.tags = kwargs.get('tags')
        self.meta = kwargs.get('meta')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.reward = Reward(**kwargs.get('reward'))

    def __str__(self):
        return '\n'.join([ '%s: %s' % (attr, self.__dict__[attr]) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('__') ])

class Reward:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.thumbnail_url = kwargs.get('thumbnail_url')
        self.point = Point(**kwargs.get('point'))
        self.begins_at = kwargs.get('begins_at')
        self.ends_at = kwargs.get('ends_at')
        self.reward_status = Reward_Status(**kwargs.get('reward_status'))

    def __str__(self):
        return '\n' + '\n'.join([ '    %s: %s' % (attr, self.__dict__[attr]) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('__') ])

class Point:
    def __init__(self, **kwargs):
        self.platinum = kwargs.get('platinum')

    def __str__(self):
        return '\n' + '\n'.join([ '        %s: %s' % (attr, self.__dict__[attr]) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('__') ])

class Reward_Status:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.limited = kwargs.get('limited')

    def __str__(self):
        return '\n' + '\n'.join([ '        %s: %s' % (attr, self.__dict__[attr]) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('__') ])

def dissect():
    apiRoutes = [] # Maybe try to dissect some of Nintendo's NSO Applet API?
    funcPattern = re.compile('([a-zA-Z0-9]+):function\(\){')
    keyPattern = re.compile('(?:key:"([a-zA-Z]+)".+?(?=method:"([a-zA-Z]+)"))+')
                            # This has problems because it doesn't check
                            # to see if the scope has changed when matching
                            # to a method
                            # hence why it's "backup"

    with open('./static/js/main.1d72eb58.js', 'r') as file:
        data = file.read()
        strings = re.findall('"([^"]*)"', data)
        for string in strings:
            if string.startswith('static/'):
                routes.append('/' + string)
            elif string.startswith('/v') or string.startswith('/preview/v'):
                apiRoutes.append(string)
        apiNames = funcPattern.findall(data)
        apiNames = apiNames[apiNames.index('getV1ApplicationsId'):apiNames.index('getV2LongRun') + 1]

        for i in range(len(apiRoutes)):
            try:
                apiRoutes[i] = Route(route = apiRoutes[i], name = apiNames[i])
            except IndexError:
                apiRoutes[i] = Route(route = apiRoutes[i])

        apiNamesBK = keyPattern.findall(data)

    with open('./api.txt', 'w') as file:
        file.write('\n'.join(map(str, apiRoutes)))

def get():
    for route in routes:
        file_route = os.path.join(os.getcwd(), route.lstrip('/'))
        folder_route = '/'.join(file_route.split('/')[:-1])
        if len(route.split('/')[-1]) == 0:
            file_route = os.path.join(os.getcwd(), 'index.html')
        if not os.path.exists(folder_route):
            os.makedirs(folder_route)
        if os.path.isfile(file_route):
            continue
        result = httpx.get(url + route, headers = headers, verify = False)
        with open(file_route, 'wb') as file:
            file.write(result.content)

def api():
    headers = {} # REDACTED

    #route = '/gifts/assets/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBa1ViIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--453441b7662b5d45a29787f73f44735b7fc90216/animal-crossing-new-horizons_2030.webp'
    #response = httpx.get(url + route, headers = headers, verify = False)
    #with open('test.webp', 'wb') as file:
        #file.write(response.content)

    # API works, but I don't have a way to replicate it without manually using dev tools at the moment
    # For the time being, I will be dissecting API calls that I have already made and downloaded
    gifts = []
    with open('gift_categories.json', 'r') as file:
        gift_categories = json.loads(file.read())
    for gift in gift_categories[0]['gifts']:
        gifts.append(Gift(**gift))
    for gift in gifts:
        route = gift.reward.thumbnail_url.replace(url, '')
        file_route = os.path.join(os.getcwd(), route.lstrip('/'))
        dest_route = os.path.join(os.getcwd(), 'gifts', gift.id + '.webp')
        folder_route = '/'.join(dest_route.split('/')[:-1])
        if not os.path.exists(folder_route):
            os.makedirs(folder_route)
        if os.path.isfile(dest_route):
            continue
        with open(file_route, 'rb') as input:
            with open(dest_route, 'wb') as output:
                output.write(input.read())
    with open(os.path.join(os.getcwd(), 'gifts/README.md'), 'w') as file:
        file.write('# Files are as below:\n\n```%s```' % '\n'.join(map(str, gifts)))

if scrape:
    get()

if jsScrape:
    dissect()

if scrape and jsScrape:
    get()

if testAPI:
    api()
