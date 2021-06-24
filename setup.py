from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Easy calculations for your needs (Beta)'
LONG_DESCRIPTION = 'Easy calculations for your daily needs and easy python highly customizable calculations (In Development | Beta)'

setup(
    name="easycalculations",
    version=VERSION,
    author="GenZ Gamer",
    author_email="<mail@indiancubingyt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['math', 'random'],
    keywords=['python', 'calc', 'calculations', 'easy', 'easycalculations'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Everyone",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)