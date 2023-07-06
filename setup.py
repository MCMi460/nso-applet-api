# Made by Deltaion Lee (MCMi460) on Github
import setuptools

setuptools.setup(
	name = 'nso-applet-api',
	version = '0.0.1',
	description = 'Nintendo NSO applet API',
	long_description = 'This library implements in Python various API endpoints from the NSO Webapplet',
	author = 'Deltaion Lee',
	author_email = '32529306+MCMi460@users.noreply.github.com',
	url = 'https://github.com/MCMi460/nso-applet-api',
	packages = [
		'nso',
	],
	package_data = {

	},
	install_requires = [
		'httpx',
		'requests',
	],
)
