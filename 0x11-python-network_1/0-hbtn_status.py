#!/usr/bin/python3

"""
python3 for url request
"""

from urllib.request import urlopen


url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    data = response.read()

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
print("\t- utf8 content: {}".format(data))
