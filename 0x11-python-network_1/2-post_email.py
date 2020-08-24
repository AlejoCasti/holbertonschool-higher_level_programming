#!/usr/bin/python3
''' script that sends a POST request '''

if __name__ == '__main__':
    import urllib.request
    from sys import argv

    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data) as response:
        html = response.read().decode('utf-8')
        print(html)
