#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import msgpack
import time
import random

def structure(identifier):
    return {
        'identifier': identifier,
        'randomvalue': random.randint(20, 40),
        'timestamp': time.time()
    }

idCounter=0
while 1:
    topack=structure(idCounter)
    print('Data before packing:\n',topack,'\n')
    pack=msgpack.packb(topack, use_bin_type=True)
    print('Data after packing:\n',pack,'\n')
    decoded = msgpack.unpackb(pack)
    print('Data after unpacking:\n',decoded,'\n')
    idCounter+=1
    print('\n\n')
    time.sleep(3)