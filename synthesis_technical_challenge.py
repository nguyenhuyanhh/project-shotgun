"""Technical challenge for Synthesis.

TASK: Create a code thats prints each the post's status and all other useful information
in the post in a manner similar to the original facebook page (separate each post with a newline)
Website: https://www.facebook.com/bobbibrown.sg/
"""

from __future__ import print_function

import json
import os

import requests
from bs4 import BeautifulSoup

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(CUR_DIR, 'config.json')


def old_crawler():
    """Crawling the Facebook page using BeautifulSoup."""
    page = requests.get("https://www.facebook.com/bobbibrown.sg/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Gets all the posts in the page
    divs = soup.find_all('div', class_="_5pcr userContentWrapper")
    for div in divs:
        print(div)


def new_crawler():
    """Crawling the Facebook page using Facebook Graph API."""
    # Get access token from config.json
    with open(CONFIG_PATH, 'r') as json_:
        config = json.load(json_)

    url = 'https://graph.facebook.com/v2.11/bobbibrown.sg/posts'
    response = requests.get(url=url, params=config).json()
    print(response)


if __name__ == '__main__':
    new_crawler()
