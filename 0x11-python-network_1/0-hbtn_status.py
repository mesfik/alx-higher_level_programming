#!/usr/bin/python3

"""
python3 for url request
"""

from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        data = response.read()

    print("Body response:")
    print("\t- type:", (type(data)))
    print("\t- content:", (data))
    print("\t- utf8 content:", data.decode("utf-8"))
