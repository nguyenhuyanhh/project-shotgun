"""Technical challenge for Synthesis.

TASK: Create a code thats prints each the post's status and all other useful information
in the post in a manner similar to the original facebook page (separate each post with a newline)
Website: https://www.facebook.com/bobbibrown.sg/
"""

from __future__ import print_function

import json
import os

import requests

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(CUR_DIR, 'config.json')
TEMP_PATH = os.path.join(CUR_DIR, 'temp.json')

GRAPH_API_HEADER = 'https://graph.facebook.com/v2.11/'
GRAPH_API_REACTIONS = ['LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']


def old_crawler():
    """Crawling the Facebook page using BeautifulSoup."""
    from bs4 import BeautifulSoup

    page = requests.get("https://www.facebook.com/bobbibrown.sg/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Gets all the posts in the page
    divs = soup.find_all('div', class_="_5pcr userContentWrapper")
    for div in divs:
        print(div)


def new_crawler(limit=100):
    """Crawling the Facebook page using Facebook Graph API."""
    import pandas as pd

    # Get access token from config.json
    with open(CONFIG_PATH, 'r') as json_:
        config = json.load(json_)
    config['fields'] = 'id,created_time,message,link,story'

    # Get posts from Graph API
    data = []
    url = GRAPH_API_HEADER + 'bobbibrown.sg/posts'
    response = requests.get(url=url, params=config).json()
    while len(data) < limit and 'paging' in response and 'next' in response['paging']:
        data += response['data']
        response = requests.get(url=response['paging']['next']).json()

    # Get post data from Graph API
    config['fields'] = 'likes.summary(1),comments.summary(1),shares,'
    config['fields'] += ','.join(['reactions.type({}).limit(0).summary(1).as(reactions_{})'.format(
        x, x.lower()) for x in GRAPH_API_REACTIONS])
    for post in data:
        url = GRAPH_API_HEADER + post['id']
        response = requests.get(url=url, params=config).json()
        for reaction in GRAPH_API_REACTIONS:
            reaction_id = 'reactions_{}'.format(reaction.lower())
            post[reaction_id] = response[reaction_id]['summary']['total_count']
        post['reactions_like'] = response['likes']['summary']['total_count']
        post['comments'] = response['comments']['summary']['total_count']
        if 'shares' in response:  # shares only available for some post types
            post['shares'] = response['shares']['count']

    # Output data to temporary file
    with open(TEMP_PATH, 'w') as json_:
        json.dump(data, json_, indent=4, sort_keys=True)

    # Output data to csv
    df_ = pd.DataFrame(data)
    df_.to_csv(os.path.join(CUR_DIR, 'output.csv'), index=False)


if __name__ == '__main__':
    from time import time

    # Measure running time
    START_TIME = time()
    new_crawler(100)
    print('Running time: {} secs'.format(time() - START_TIME))
