#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:29:02 2020

@author: saroshamomin
"""
#%%
age = int(input("What is your age? "))
if age >= 18:
    print("Congrats! You are old enough to vote")
else:
    print("You are not old enough to vote.")
print("The November election has passed. There is a new president.")

#%%
temperature = float(input("What is the temperature? "))
if temperature < 40:
    print("A little cold isn't it? ")
    print("Please bring a jacket. ")     # Pay attention to the indentation 
else:                                   # Do not need a condition for else
    print("Nice weather we're having. ")
    print("You do not need to bring a jacket. ")

#%%
hours_worked = int(input("How many hours did you work? "))
pay_rate = float(input("What is your pay rate? ")) 

if hours_worked > 40:
    total_pay = ((hours_worked - 40) * (pay_rate * 1.5)) + (40 * pay_rate)
    print("Your total pay is $", total_pay, sep='')
else:
    total_pay = hours_worked * pay_rate
    print("Your total pay is $", total_pay, sep='')

#%%
