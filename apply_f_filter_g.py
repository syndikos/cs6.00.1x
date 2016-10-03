# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:07:15 2016

@author: YHWH
"""


def applyF_filterG(L, f, g):
    new_list = L[:]
    for i in new_list:
        try:
            if g(f(i)) == False:
                L.remove(i)
        except:
            L.remove(i)
            
    if len(L) == 0:
        return -1
    else:
        return max(L)
        
        
def f(i):
    return  2 / i
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)