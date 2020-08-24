#!/usr/bin/python3
''' Script that fetches web page '''

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        encod = html.decode('utf8')
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', encod)
