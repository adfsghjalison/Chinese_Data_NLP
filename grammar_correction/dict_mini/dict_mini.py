# coding=utf-8
import os, sys, json

script_dir = os.path.realpath(__file__).rsplit('/', 1)[0]
d1 = json.load(open(os.path.join(script_dir, 'character_zhuyin')))
d2 = json.load(open(os.path.join(script_dir, 'zhuyin_character')))

def get_zhuyin(c):
    return d1[c]

def get_characters(p):
    return d2[p]

def homophone(c):
    return get_characters(get_zhuyin(c))

