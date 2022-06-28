from setuptools import find_packages, setup

import versioneer

DISTNAME = "cog_data"
LICENSE = "MIT"
AUTHOR = "Justin Goodwin, Ryan Soklaski"
AUTHOR_EMAIL = "rsoklaski@gmail.com"
URL = "https://github.com/rsokl/cog_data"
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Scientific/Engineering",
]
KEYWORDS = (
    "download utilities"
)
INSTALL_REQUIRES = [
    "pooch >= 1.6.0",
    "typing-extensions >= 4.1.0",
]

DESCRIPTION = "Simple functions for downloading and accessing data for CogWorks"


setup()