# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
print("sarosha momin")
print('next to you ')
print("I can't believe I'm coding!")

length = 15
height = 12
area = length * height 

print(" the length is ", length)
print(" the height is ", height)
print(" the length is ", length - 5)
print(" the height is ", height + 6)

class_name = "mis 304"
print(class_name)

first_name = "sarosha"
last_name = "momin"

print(first_name, last_name)

print(9/4)
print(9//4)
print(9%4)
print(-9//4)
print(10/5 + 4)
print((2 + 1)* 6//4)

#%%
have_coded = int(input("how many students have coded before "))
never_coded = int(input("how many students have never coded before "))
total_students = have_coded + never_coded
# can do this if i want for both data types but is it more efficient idk
# coded_percentage = have_coded/total_students * 10
# code_before = int(have_coded/total_students * 100)
# print("the percentage of students who have coded before is ", code_before)
print("the percentage of students who have coded before is ", have_coded/total_students * 100)
print("the percentage of students who have coded before is ", int(have_coded/total_students * 100))

#%%
hours_worked = float(input("how many hours did you work "))
pay_rate = float(input("what is your pay rate "))
print("your total pay is", hours_worked * pay_rate)
#%%
print ("A", end = ' ')
print ("B", end = ' ')
print("A", "B", "C")
print ("A", "B", sep = '*')
print('Mon\tTues\nWed')
print(format(5000 / 3, ',.2f'))
#%%
feet = int(input("please enter the feet "))
inches = int(input("please enter the inches "))
feet_to_inch = 12
inch_to_centimeter = 2.54
total_inches = feet * feet_to_inch + inches
total_centi = total_inches * inch_to_centimeter
print("the initial length is ", feet, " feet and ", inches, " inches." )
print("the total number of inches is ", total_inches)
print("the total number of centimeters is ", format(total_centi, '.2f'))

#%%
#Write a program that calculates the total amount of a meal purchased at a restaurant. 
#The program should ask the user to enter the charge for the food, then calculate the amounts of a18 
#percent tip and 7 percent sales tax. Display each of these amounts and the total.






#%%
#A company has determined that its annual profit is typically 23 percent of total sales. The company’s 
#total sales increases by 10% every year. Write a program that asks the user to enter the projected 
#amount of total sales of 2020, then displays the profit that will be in 2023. 











