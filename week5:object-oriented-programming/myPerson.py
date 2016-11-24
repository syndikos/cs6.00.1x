#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:44:19 2016

@author: guilin
"""
import datetime

class Person(object):
    def __init__(self, name):
        """ create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split('  ')[-1]

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        """return last name"""
        return self.lastName

#class Person(object):
#    def __init__(self, name):
#        """create a class called name"""
#        self.name = name
#        self.birthday = None
#        self.lastName = name.split(' ')[-1]
#
    def __str__(self):
        """return self's name"""
        return self.name
    



    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, and False otherwise"""

        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        

class MITPerson(Person):
    nextIDNum = 0 # next id number to assign
    def __init__(self, name):
         Person.__init__(self, name) # initialize Person attributes
         self.idNum = MITPerson.nextIDNum # MITPerson attribute: unique ID
         MITPerson.nextIDNum += 1

    def getIdNum(self):
        return self.idNum
    # sort MIT people by ID not name.
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + 'says:' + utterance)
        
        
class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, 'dude, '+utterance)
    

class Grad(MITPerson):
    pass

    def isStudent(obj):
        return isinstance(obj, UG) or isinstance(obj, Grad)


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Arash Ferdowsi', 2018)
s4 = Grad('Drew Houston')
s5 = UG('Mark Zuckerberg', 2019)


studentList = [s1, s2, s3, s4, s5]