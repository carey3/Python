#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1, 2, 3, 4, 5]
print(f'x is {format(x)} and type {type(x)}')
if isinstance(x, tuple):
    print('is a tuple')
elif isinstance(x, list): 
    print('is a list')
elif isinstance(x,dictionary): 
    print('is a dictionary')
else:
    print('is not a built in type')

x = 7
print(f'x is {format(x)} and type {type(x)}')

x = 7.1
print(f'x is {format(x)} and type {type(x)}')

x = True
print(f'x is {format(x)} and type {type(x)}')

x = False
print(f'x is {format(x)} and type {type(x)}')

x = 7 > 5
print(f'x is {format(x)} and type {type(x)}')

x = None
print(f'x is {format(x)} and type {type(x)}')

x = "None"
print(f'x is {format(x)} and type {type(x)}')

x = 0
print(f'x is {format(x)} and type {type(x)}')

x = ""
print(f'x is {format(x)} and type {type(x)}')

