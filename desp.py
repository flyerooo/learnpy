#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/8 8:51

class NonNeg:
    def __init__(self, default = 0):
        self.default = default
    def __get__(self, instance, owner):
        return self.default
    def __set__(self, instance, val):
        if val > 0:
            self.default = val
        else:
            print("The value must be NonNegative!")
    def __delete__(self, instance):
        pass
class Movie:
    rating = NonNeg()
    score = NonNeg()
if __name__ == "__main__":
    m = Movie()
    print ("rating:",m.rating)
    print ("score:",m.score)
    m.rating = 80
    print ("rating:",m.rating)
    m.score = -3
    print ("score:",m.score)

