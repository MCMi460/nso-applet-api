# mega script by Deltaion Lee (MCMi460)
import os, subprocess, re

# headers, etc
url = 'https://lp1.nso.nintendo.net'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519',
    'accept-language': 'en-US,en;q=0.5',
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

# For API dissection
class Route:
    def __init__(self, *, route = '', name = '', method = ''):
        self.route = route
        self.name = name
        self.method = method

    def __str__(self):
        return '%s: %s \'%s\'' % (self.route if self.route else 'no route supplied', self.method if self.method else 'no method supplied', self.name if self.name else 'no name supplied')

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
        result = subprocess.getoutput('curl --http2 %s -k %s -o %s' % (' '.join( '--header "%s: %s"' % (h, headers[h]) for h in headers.keys()), url + route, file_route))

if scrape:
    get()

if jsScrape:
    dissect()

if scrape and jsScrape:
    get()
