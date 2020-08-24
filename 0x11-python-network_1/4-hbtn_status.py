#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import requests
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.text)
