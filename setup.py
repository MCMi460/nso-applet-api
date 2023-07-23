# Made by Deltaion Lee (MCMi460) on Github
import setuptools

from pathlib import Path
directory = Path(__file__).parent
long_description = (directory / 'README.md').read_text()

setuptools.setup(
	name = 'nso-applet-api',
	version = '0.0.23',
	description = 'Nintendo NSO Applet API',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
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
