#!/usr/bin/python3
"""
2-post_email module
Post an email - urllib headers
"""


import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    Email = sys.argv[2]

    value = {'email': Email}

    response = requests.post(url, data=value)
    html = response.text
    print(html)
