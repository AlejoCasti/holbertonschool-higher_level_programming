#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    cha = sentence[0] if len_s != 0 else None
    return (len_s, cha)
