#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

print()

for n in range(333):
    if isprime(n):
        print(f'{n}', end= ' ', flush=True )
 
print()
