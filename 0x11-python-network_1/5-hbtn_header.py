#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers['X-Request-Id'])
