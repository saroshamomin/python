#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:36:33 2020

@author: saroshamomin
"""

#Review


grade_list= [[98, 76, 89, 67], [90, 65, 86, 100]]
print(grade_list[0][1])
print(grade_list[0][:2])
print(grade_list[0][1:3])
print(len(grade_list))
total = 0
count = 0
for row in range(len(grade_list)):
    for col in range(len(grade_list[0])):
        total += grade_list[row][col]
        count += 1
avg = total/count
print(avg)
#%%
set1 = set([10, 20, 30])
set2 = set([20, 30, 40])
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set1.discard(10)
print(set1)
set1.add(10)
print(set1)
set1.update([40,50,60])
print(set1)
#%%
dwarf_dict = {'Grumpy' : 111, 'Happy': 222, 'Sleepy': 333}
print(dwarf_dict['Sleepy'])
dwarf_dict['Sneezy'] = 555
for key in dwarf_dict:
    print(key, dwarf_dict[key])
dwarf_dict['Sneezy'] = 444
del dwarf_dict['Grumpy']
print(dwarf_dict)
print(dwarf_dict.items())
#%%
num = [5,10,15,20,25]
size = len(num)
count = 0
file = open('numfile.txt', 'w')
while count < size:
    num[count] -= 4
    print(num[count])
    count += 1
file.write(str(num) + '\n')
file.close()
print(num)
#%%
old_list= [1,2,3,4,5]
cnt = 0
new_list = []
for num in old_list:
    new_list.append(num)
print(new_list)
for num in old_list:
    old_list[cnt] *= 10
    cnt += 1
print(old_list)
#%%














