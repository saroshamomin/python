#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 07:58:19 2020

@author: saroshamomin
"""

name = 'Charlotte Hale'
char1 = name[0]
char2 = name[10]
print(char1, char2)
print(len(name))
#%% slicing
name = 'John Jacob Jingleheimer Schmidt'
first = name[:4]
second = name[5:10]
print(second)
third = name[11:23]
print(third)
last = name[24:]
print(last, ", ", first, sep = '')
#%%
name = 'Mickey Mouse'
if 'Mick' in name:
    print("Mick appears in", name)
    
if 'A' not in name:
    print("The letter 'A' does not appear in", name)
#%%
name = 'John Jacob JingleheimerSchmidt'
name_list = name.split()
print(name_list)
address = '123 Main St*Austin*TX*78705'
address_list = address.split('*')
for item in address_list:
    print(item)
#%%
phonebook_dict = {'Clint':'505-2612','Katie':'505-3451'}
print(phonebook_dict)

quiz_dict= {'jwt254':[83, 92, 89], 'fkw928':[85, 94, 96]}
print(quiz_dict)

test_dict= {}
print(test_dict)
#%%
phonebook_dict= {'Clint':'505-2612','Katie':'505-3451'}
print(phonebook_dict['Katie'])                #accessing a key
#%% using loops with dictionaries
phonebook_dict = {'Clint':'505-2612','Katie':'505-3451'}
for key in phonebook_dict:
    print(key) 

for key in phonebook_dict:
    print(key, phonebook_dict[key])
#%% adding elements to dictionaries
phonebook_dict = {'Clint':'505-2612','Katie':'505-3451'}
phonebook_dict['Caryn'] = '505-2662'
print(phonebook_dict)
print(len(phonebook_dict))
#%% updating elements
phonebook_dict = {'Clint':'505-2612','Katie':'505-3451'}
phonebook_dict['Clint'] = '471-4832'
print(phonebook_dict)
#%%
phonebook_dict = {'Clint':'505-2612','Katie':'505-3451'}
del phonebook_dict['Clint']
print(phonebook_dict)
print(len(phonebook_dict))

#%%






