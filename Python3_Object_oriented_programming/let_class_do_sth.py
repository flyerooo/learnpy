#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/10 12:31

# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
#
# p =Point()
# Point.reset(p)
# print(p.x, p.y)

import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
                (self.x - other_point.x) ** 2 +
                (self.y - other_point.y) ** 2
        )

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)
# print(point1.x,point1.y,point2.x,point2.y)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) ==
        point1.calculate_distance(point2))
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))