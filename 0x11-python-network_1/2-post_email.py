#!/usr/bin/python3

"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


from urllib.request import urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    data = urlencode(data).encode("utf-8")

    with urlopen(url, data) as response:
        html = response.read().decode("utf-8")

    print("Your email is: {}".format(email))
