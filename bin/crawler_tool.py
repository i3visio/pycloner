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

__version__ = "0.1.0"

import argparse
import urllib

from pycloner.crawler import Crawler
from pycloner.utils import error, warning, success, info, safelyCreateDirectories


def getParser():
    """Grabbing the parser for the arguments.
    """
    parser = argparse.ArgumentParser(description='crawler.py - A tool to crawl the content of a website and clone it.', prog='crawler.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-u', '--url', metavar='<URL>', action='store', help = 'the URL to be crawled.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which the application will process the identified profiles.')
    groupProcessing.add_argument('-d', '--depth', metavar='<depth>', required=False, default=1, action='store', type=int, help='depth of the crawling process. By default: 1.')
    groupProcessing.add_argument('-f', '--data_folder', metavar='<name>', required=False, default="./tmp", action='store', help='the name for the crawling project. By default: ./tmp')
    groupProcessing.add_argument('-p', '--project_name', metavar='<name>', required=False, default="website_crawled", action='store', help='the name for the crawling project. By default: website_crawled.')

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    #groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +" " +__version__, help='shows the version of the program and exists.')

    return parser


if __name__ == "__main__":
    # Grabbing the parser
    parser = getParser()

    args = parser.parse_args()

    if args.license:
        print(info("Showing the contents of the license..."))
        print(urllib.urlopen("https://www.gnu.org/licenses/gpl-3.0.txt").read())
        print(info("The license can be downloaded from https://www.gnu.org/licenses/gpl-3.0.txt"))
        print(info("Exiting..."))
    else:
        info("Starting the crawling process...")
        # Instatiating the crwaler
        crawler = Crawler(args.url, args.project_name, args.data_folder)
        # Starting the crawling process
        crawler.crawl()
        print(success("Finished crawling for " + args.url))

        print(info("Links crawled: " + str(len(Crawler.visited_links))))
        for link in Crawler.visited_links:
            print(success(link))

        if len(Crawler.error_links) == 0:
            print(info("Links with errors: 0"))
        else:
            print(info("Links with errors: " + str(len(Crawler.error_links))))
            for link in Crawler.error_links:
                print(error(link))
