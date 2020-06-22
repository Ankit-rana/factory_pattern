from setuptools import setup

setup(
    name='snek',
    version='0.0.1',
    entry_points = {
        'console_scripts': ['snek = src.snek:main',],
    } 
)

