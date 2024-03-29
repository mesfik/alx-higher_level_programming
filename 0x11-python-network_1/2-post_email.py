#!/usr/bin/python3
"""
2-post_email module
Post an email - urllib headers
"""


from urllib import request, parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    Email = sys.argv[2]

    value = {'email': Email}

    data = parse.urlencode(value)
    data = data.encode('ascii')

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()

    html = html.decode('utf-8')
    print(html)
