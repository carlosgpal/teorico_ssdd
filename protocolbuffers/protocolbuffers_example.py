#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import time
import random
import structure_pb2

idCounter=0
while 1:
    structure = structure_pb2.Struct()
    structure.identifier = idCounter+1
    structure.randomvalue = random.randint(20, 100)
    structure.timestamp = time.time()
    structure.type = 2
    
    topack=structure
    print('Data before packing:\n',topack,'\n')
    pack = topack.SerializeToString()
    print('Data after packing:\n',pack,'\n')
    structure = structure_pb2.Struct()
    structure.ParseFromString(pack)
    print('Data after unpacking:\n',structure,'\n')
    idCounter+=1
    print('\n\n')
    time.sleep(3)