#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:43:42 2020

@author: saroshamomin
"""

# You prompt the user to enter the annual amount due. You compute the monthly amount due based on the 
# annual one. 

annual_amt = float(input("What is the annual amount due? "))
monthly_amt = annual_amt/12

print("The monthly amount due is $", format(monthly_amt, '.2f'), sep = '')

#%%

# Write a program gets three test scores and displays their average. Congratulates the user if the 
# average is a higher than 95. 

score1 = int(input("What is the first test score? "))
score2 = int(input("What is the second test score? "))
score3 = int(input("What is the third test score? "))
average = (score1+score2+score3)/3

if average >= 95:
    print("\nCongratulations! Your average is a", average)
else:
    print("\nYour average is a", average)
    
#%% 

# Write a program to prompt the user to enter two names. Print the two names in alphabetical order. 

name1 = str(input("What is the first name? "))
name2 =str(input("What is the second name? "))
print()

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
    
#%%

# Your task is to write a program to assist a technician in the process of checking a substance's 
# temperature. The maximum temperature is 102.5. Your code will finish the following: 
# Prompt the technician to enter the substance's Celsius temperature. 
# If the entered temperature is higher than the 102.5, prompt the technician to enter the temperature again. 
# Repeat step 2 until the entered temperature is acceptable, and print the temperature is acceptable. 


temp = float(input("Please enter the substance's temperature in Celsius: "))

while temp > 102.5:
    print("The maximum temperature is 102.5 Celsius.")
    temp = float(input("Please enter the substance's temperature in Celsius: "))
print("The temperature is acceptable. ")

#%%







