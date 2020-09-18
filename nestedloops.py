#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:05:05 2020

@author: saroshamomin
"""
#%%
# determining voter eligibility based on age only
age = int(input("What is your age? "))
if age >= 18:
    print("Congrats! You are old enough to vote")
else:
    print("You are not old enough to vote.")
print("The November election has passed. There is a new president.")

#%%
# determining how the weather is.
temperature = float(input("What is the temperature? "))
if temperature < 40:
    print("A little cold isn't it? ")
    print("Please bring a jacket. ")     # Pay attention to the indentation 
else:                                   # Do not need a condition for else
    print("Nice weather we're having. ")
    print("You do not need to bring a jacket. ")

#%%
# find the total pay depending on whether or not they worked pvertime the pay rate may differ. 
hours_worked = int(input("How many hours did you work? "))
pay_rate = float(input("What is your pay rate? ")) 

if hours_worked > 40:
    total_pay = ((hours_worked - 40) * (pay_rate * 1.5)) + (40 * pay_rate)
    print("Your total pay is $", total_pay, sep='')
else:
    total_pay = hours_worked * pay_rate
    print("Your total pay is $", total_pay, sep='')


#%% Bonus Exercise
# Guppies are hardy fish, but they can’t live in all water temperatures. The acceptable range for 
# guppies is between 72 and 86 degrees Fahrenheit.Write a program that asks the user for a temperature. 
# Then display one of two messages based on the information provided: You’re going to freeze your guppy! 
# You’re going to boil your guppy!

temp = float(input("What is the temperature of your water? "))

if temp > 86:
    print("You're going to boil your guppy!")
elif temp < 72:
    print("You're going to freeze your guppy!")
else:
    print("Your guppy is going to be happy!")
    

#%%
# relational operators: AND, OR, NOT
# compare swings using: == and != OR relative values (useful for sorting): >, >=, <, <= or ASCII values

fruit = str(input("Would you like grapes or papayas? Please enter G for grapes and P for papayas. "))
if fruit == 'G' or fruit == 'P':
    print("You have selected ", fruit)
else: 
    print("Invalid choice! You have selected ", fruit)
    
#%%
# determining eligibility for a scholarship based on gender and ethnicity
gender = str(input("Please enter your gender. (M or F) "))
minority = str(input("Are you a minority? (Y or N) "))

if gender == 'F' or minority == 'Y':
    print("You are eligible for a scholarship. Please apply. ")
else: 
    print("You are not eligible for a scholarship. Blame your parents. ")
    
    
#%%
# whether or not you will suceed in class depending on if you do/don't come to class or don't/do your homework
come_to_class = str(input("Do you come to class, Y or N? "))
do_homework = str(input("Do you do your homework, Y or N? "))
if come_to_class == 'Y':
    if do_homework == 'Y':
        print("You will be successful.")
    else:
        print("You will not be successful.")
else:
    if do_homework == 'Y':
        print("Still succeed.")
    else:
        print("Fail.")
        
#%%
# can use elif which is like saying else if
# calculate what your letter grade is based on your numerical grade.
grade = float(input("What is your course grade? "))

if grade > 100:
    print("The grade you have entered is invalid. ")
elif grade >= 90:
    print("Your letter grade is A.")
elif grade >= 80:
    print("Your letter grade is B.")
elif grade >= 70: 
    print("Your letter grade is C.")
elif grade >= 60:
    print("Your letter grade is D.")
elif grade < 60:
    print("Your lettter grade is F.")


#%% Bonus exercise

major = str(input("Are you an MIS major? Type Y for yes or N for no. "))
wrong_answer = 2

if major != 'Y' and major != 'N': 
    wrong_answer = 88888
elif major =='Y':
    subsidy = 50.00
else: 
    subsidy = 20.00

if wrong_answer == 88888:
    print("Due to incorrect input, no gift certificate is offered.")
else: 
    print("You will receive a $", format(subsidy, '.02f'), " gift card. ", sep = '')


#%%















