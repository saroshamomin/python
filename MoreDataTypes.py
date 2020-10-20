#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:44:27 2020

@author: saroshamomin
"""

#examples of lists being different data types
grade_list= [98, 76, 89, 90, 65, 86]
name_list= ['Mickey Mouse', 'Cinderella', 'Wall-E']
employee_list= ['Jon Smith', 65000.00, 24]
course_list= []

#%%
for grade in grade_list:
    print(grade)
    
print(grade_list)

#%%
print(grade_list[0])
print(grade_list[5])
# print(grade_list[6])       wont work
size = len(grade_list)
print(size)
#%%
count= 0
while count < size:
    print (grade_list[count])
    count+=1
#%%
print(grade_list[1:4])
print(grade_list[:3]) #gives everything from 0 to 3 not inclusive
print(grade_list[3:]) #gives everything from index 3 onwards
print(grade_list[1:5:2])
#%%
old_list= [1,2,3]
old_list[2] = 10
print(old_list)
#%%
new_list= [1,2,3] + [4,5,6]          #cannot do with diff data types
print(new_list)
Output: [1,2,3,4,5,6]
#%%
name_list= ["Belle", "Gaston", "Beast"]
name = input("Enter a character’s name: ")
if name in name_list:
    print(name, "was found in the list")
else:
    print(name, "was not found in the list")
#%%
numberlist = [5,10,15,20,25]
cnt = 0
numberfile = open('numberfile.txt', 'w')
size = len(numberlist)
while cnt < size:
    numberlist[cnt] -= 4
    print(numberlist[cnt])
    cnt += 1
numberfile.write(str(numberlist) + '\n')
print(numberlist)
#%%   

    
    
    
    