#!/usr/bin/python3
''' Script that gets header info from page '''

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.URLError as e:
        print('Error code:', e.code)
