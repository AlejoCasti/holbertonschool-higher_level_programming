#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """ text indentation """
    cont = 0
    if type(text) is not str:
        raise TypeError('text must be a string')
    for idx, i in enumerate(text):
        if i in ['.', '?', ':']:
            if idx + 1 < len(text) - 1:
                if text[idx + 1] is " ":
                    text = text[:(idx + cont) + 1] + '\n\n'\
                           + text[(idx + cont) + 2:]
                else:
                    text = text[:(idx + cont) + 1] + '\n\n'\
                           + text[(idx + cont) + 1:]
                cont += 1
            else:
                text = text[:(idx + cont) + 1] + '\n\n'
    print(text, end='')
