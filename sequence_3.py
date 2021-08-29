#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def arrayPrint(x=1):
    cnt = 0
    for i in x:
        print('count is {}, i is {}'.format(cnt, i))
        cnt+=1
    print()
    
    
print('This is a List, it is mutable')
x = [ 1, 2, 3, 4, 5 ] # this is a mutable list
x[2] = 7
arrayPrint(x)

print('This is a tuple, it is not mutable')
x = ( 1, 2, 3, 4, 5 ) # this is a not mutable list
#x[2] = 7   # can't change this type of list
arrayPrint(x)

print('This is a tuple using the range, it is not mutable')
x = range(1,6)   #range(start, end, step) or range(start, end) or range(end)
arrayPrint(x)

print('to make a range mutable, make it a list with list(range(1,6)).')
x = list(range(1,6))   #range(start, end, step) or range(start, end) or range(end)
x[4] = 7
arrayPrint(x)

# a dictionary
print('This is a dictionary, it is also mutable')
x = { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
x['six'] = 6
for k, v in x.items():
    print(f'key: {k}, value: {v}')
#   print('key: {}, value: {}'.format(k, v))
print()
