#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/14 0:00

def isPrime(num):
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
