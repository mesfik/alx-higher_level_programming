#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""


from urllib.request import urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        X_Request_Id = response.getheader('X-Request-Id')
        html = response.read()

    print(X_Request_Id)
