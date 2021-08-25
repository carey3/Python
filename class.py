#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quaaack!'
    walks = 'Walks like a duck.'
    
    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walks)

def main():
    print()
    donald = Duck()
    donald.quack()
    donald.walk()
    print()
    
if __name__ == '__main__': main()
