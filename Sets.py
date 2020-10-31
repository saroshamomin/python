#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:04:16 2020

@author: saroshamomin
"""

letter_set = set(['a','b','c'])
string_set = set('abc')
another_string_set = set('aabbbccc')
new_set = set(['abc'])
word_set= set(['one','two','three'])
print(word_set)
#%%
letter_set= set(['a','b','c'])
letter_set.add('def')
print(letter_set)
set1 = set([12, 24, 36])
set2 = set(['one','two','three'])
set1.update(set2)
print(set1)
#%%
letter_set= set(['a','b','c'])
letter_set.remove('c')
print(letter_set)
set1 = set([12, 24, 36])
set1.discard(12)
set1.remove(12)
print(set1)
#%%
name_set= set(['Clint','Katie', 'Caryn'])
for name in name_set:
    print(name)
#%%
set1 = set(['a','b','c'])
set2 = set(['c','d','e'])
set3 = set1.union(set2)
print(set3)
set1 = set([12, 24, 36])
set2 = set([48, 24, 12])
set3 = set1.union(set2)
print(set3)
print(type(set1))
#%%
set1 = set(['a','b','c'])
set2 = set(['c','d','e'])
set3 = set1.intersection(set2)
print(set3)
set1 = set([12, 24, 36])
set2 = set([48, 24, 12])
set3 = set1.intersection(set2)
print(set3)
#%%











