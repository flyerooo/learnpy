#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/14 14:08

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['hello2'] = 12
print(longkeys.longest_key())
