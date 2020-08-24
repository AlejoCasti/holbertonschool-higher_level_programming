#!/usr/bin/python3
''' Script that gets header info from page '''

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    try:
        response = urllib.request.urlopen(argv[1])
        html = response.read()
        print(html)
    except urllib.error.URLError as e:
        print('Error code: ', e.code)
