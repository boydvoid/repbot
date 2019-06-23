from setuptools import setup
setup(
    name = 'repbot',
    version = '0.1.0',
    packages = ['repbot'],
    entry_points = {
        'console_scripts': [
            'repbot = repbot.__main__:main'
        ]
    })