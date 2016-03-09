#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/7 13:30

def main():
    myCount = Count()
    times = 0
    for i in range(0, 100):
        increment(myCount, times)
    print("myCount.count =", myCount.count, "times=", times)

def increment(c, times):
    c.count += 1
    times += 1
class Count:
    def __init__(self):
        self.count = 0
main()