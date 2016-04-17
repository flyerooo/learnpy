#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/14 11:39

class ContactList(list):
    def search(self, name):
        '''Return all contents that contain the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact("John A", "johna@xx.xx")
c2 = Contact("John B", "johnb@xx.xx")
c3 = Contact("John C", "johnc@xx.xx")

print([c.name for c in Contact.all_contacts.search('John')])
print([c.name for c in Contact.all_contacts])