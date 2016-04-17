#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/14 11:52

class Contact:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "{} order to {}".format(order, self.name))

c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
# print(c.name, c.email, s.name, s.email)
print([(c.email+c.name) for c in Contact.all_contacts])
# print(s.order("T need pliers"))