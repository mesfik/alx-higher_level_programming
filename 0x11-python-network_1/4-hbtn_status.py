#!/usr/bin/python3

"""
python3 for url request
"""

import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    html = response.text

    print("Body response:")
    print("\t- type:", (type(html)))
    print("\t- content:", (html))
