try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'TODO',
    'author': 'iTrust',
    'url': 'https://github.com/scy-phy/minicps',
    'download_url': 'https://github.com/scy-phy/minicps',
    'author email': 'abc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'package': ['minicps'],
    'scripts': [],
    'name': 'minicps'
}


setup(**config)