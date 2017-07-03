#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of Pycloner. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero  General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Importing the temporal scripts for the setup and taking the new version number
import pycloner
from pycloner.utils import error, warning, success, info

NEW_VERSION = pycloner.__version__

print(info("Launching the pycloner module setup.py..."))

# Launching the setup
setup(
    name="pycloner",
    version=NEW_VERSION,
    description="pycloner is a package that tries to help in the process of manually crawling a website.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/pycloner",
    license="COPYING",
    keywords = "python osint harvesting crawling cloning",
    scripts= [
        "bin/crawler_tool.py"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    packages=[
        "pycloner",
    ],
    install_requires=[
        "beautifulsoup4>=4.6.0",
        "colorama"
    ],
)

print(success("setup.py correctly run for pycloner."))
print(info("You can find additional information on how to use this package in <https://github.com/i3visio/pycloner>."))
