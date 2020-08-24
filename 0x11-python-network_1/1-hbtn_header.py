#!/usr/bin/python3
''' Script that gets header info from page '''

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()['X-Request-Id']
        print(html)
