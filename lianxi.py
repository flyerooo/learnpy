#coding=utf-8
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def color(self, color):
        print "%s is %s" % (self.name,color)


girl = Person('cangloashi')

name =girl.getName()