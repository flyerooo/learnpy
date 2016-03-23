#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 3:05
from tqdm import trange
from time import sleep

for i in trange(10, desc='1st loop', leave=True):
    for j in trange(5, desc='2nd loop', leave=True, nested=True):
        for k in trange(100, desc='3nd loop', leave=True, nested=True):
            sleep(0.01)