#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    values = {'email' : argv[2]}
    response = requests.post(url, values)
    print(response.text)
