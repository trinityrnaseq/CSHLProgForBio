#!/usr/bin/env python3

import sys

def decorate_name_val(name_val):
    decorated = " ".join([get_unicorn(), name_val, get_unicorn()])
    return(decorated)

def get_unicorn():
    # returns unicorn symbol
    return("\U0001f984")


if __name__ == '__main__':
    print("my_module.py running as driver: ", decorate_name_val(__name__))

