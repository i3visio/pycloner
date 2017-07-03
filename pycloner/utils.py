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

import colorama
colorama.init(autoreset=True)

def colorize(text, type=None):
    """Function that colorizes a message. Possible options for type: ["ERROR", "WARNING", "SUCCESS", "INFO"]
    """
    if type == "ERROR":
        return colorama.Fore.RED + "[XX] > " + text
    elif type == "WARNING":
        return colorama.Fore.YELLOW + "[??] > " + text
    elif type == "SUCCESS":
        return colorama.Fore.GREEN + "[OK] > " + text
    elif type == "INFO":
        return colorama.Fore.BLUE + "[!!] > " + text
    else:
        return text


def error(text):
    return colorize(text, "ERROR")


def warning(text):
    return colorize(text, "WARNING")


def success(text):
    return colorize(text, "SUCCESS")


def info(text):
    return colorize(text, "INFO")


def safelyCreateDirectories(path, type="FILE"):
    """It safely creates the directories tree for a file or directory path.
    """
    if type == "FILE":
        directory = os.path.dirname(path)
    elif type == "DIRECTORY":
        directory = path

    if not os.path.exists(directory):
        os.makedirs(directory)
