#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def arrayPrint(x=1):
    for i in x:
        print('i is {}'.format(i))
    print()
    
x = [ 1, 2, 3, 4, 5 ] # this is a mutable list
x[2] = 7
arrayPrint(x)

x = ( 1, 2, 3, 4, 5 ) # this is a non mutable list
#x[2] = 7   # can't change this type of list
arrayPrint(x)

x = range(1,6)
arrayPrint(x)

# a dictionary\
x = { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
x['six'] = 6
for k, v in x.items():
    print('key: {}, value: {}'.format(k,v))
print()
