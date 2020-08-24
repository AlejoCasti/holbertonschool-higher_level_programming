#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    if response.status_code > 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)
