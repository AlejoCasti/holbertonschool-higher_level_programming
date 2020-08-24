#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    js = response.json()
    print(js.get('id'))
