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
# calculating how many students have coded before with different data types. 
have_coded = int(input("How many students have coded before? "))
never_coded = int(input("How many students have never coded before? "))
total_students = have_coded + never_coded
code_before_float = have_coded/total_students * 100
code_before = int(have_coded/total_students * 100)
print("The percentage of students who have coded before is ", code_before_float, "%", sep = '')
print("The percentage of students who have coded before is ", code_before, "%", sep = '')

#%%
# calculating total pay
hours_worked = float(input("How many hours did you work "))
pay_rate = float(input("What is your pay rate "))
print("Your total pay is", hours_worked * pay_rate)
#%%
# how to format outputs
print ("A", end = ' ')
print ("B", end = ' ')
print("A", "B", "C")
print ("A", "B", sep = '*')
print('Mon\tTues\nWed')
print(format(5000 / 3, ',.2f'))
#%% 
# converting feet to inches exercise

feet = int(input("Please enter the feet. "))
inches = int(input("Please enter the inches. "))
feet_to_inch = 12
inch_to_centimeter = 2.54
total_inches = feet * feet_to_inch + inches
total_centi = total_inches * inch_to_centimeter
print("The initial length is ", feet, " feet and ", inches, " inches." )
print("The total number of inches is ", total_inches)
print("The total number of centimeters is ", format(total_centi, '.2f'))

#%%
#Write a program that calculates the total amount of a meal purchased at a restaurant. 
#The program should ask the user to enter the charge for the food, then calculate the amounts of a18 
#percent tip and 7 percent sales tax. Display each of these amounts and the total.

food_total = float(input("How much did the food cost all together? "))
tip_rate = 0.18
tax_rate = 0.07
tip = float(food_total * tip_rate)
tax = float(food_total * tax_rate)
print("Cost of meal: $", format(food_total, '.2f'), sep = '')
print("Tips: $", format(tip, '.2f'), sep = '')
print("Sales tax: $", format(tax, '.2f'), sep = '')
print("Total amount: $", format(food_total + tip + tax, '.2f'), sep = '')




#%%
#A company has determined that its annual profit is typically 23 percent of total sales. The company’s 
#total sales increases by 10% every year. Write a program that asks the user to enter the projected 
#amount of total sales of 2020, then displays the profit that will be in 2023. 

total_sales = float(input("What is the projected amount of total sales for 2020? "))
increase_rate = 1.10
profit = (increase_rate ** 3) * total_sales * .23
print("Your profit for 2023 is estimated to be $", format(profit, '.2f'), sep = '')


