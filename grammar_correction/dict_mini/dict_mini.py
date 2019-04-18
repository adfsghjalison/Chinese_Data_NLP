# coding=utf-8
import json

d1 = json.load(open('character_zhuyin'))
d2 = json.load(open('zhuyin_character'))

def get_zhuyin(c):
    return d1[c]

def get_characters(p):
    return d2[p]

def homophones(c):
    return get_characters(get_zhuyin(c))

print(homophones("逼"))

