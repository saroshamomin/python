#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:01:19 2020

@author: saroshamomin
"""

#%% example
enter_loop= 1
while enter_loop== 1:    
    print('Learning loop is fun!')    
    enter_loop= int(input('Do you want to print another statement? '))
print('Outside of Loop')

#%%

number = 0
while number < 5:
    print("Number is", number)
    number += 1  #prevents inifinite loop
    
#%%

number = int(input("Please enter a number: "))
product = number * 10

while product < 100:
    print(number, "times 10 is", product)
    number = int(input("Please enter a number: "))
    product = number * 10
    
    
#%%

lb_to_kg = str(input("Would you like to convert your weight to kilograms? Enter Y for yes or N for no. "))
CONV_RATE = 0.4536

while lb_to_kg == 'Y':
    weight_lb = float(input("Enter your weight in pounds. "))
    weight_kg = CONV_RATE * weight_lb
    print("Your new weight in kilograms is ", format(weight_kg, '.02f'))
    lb_to_kg = str(input("Would you like to do another conversion? Enter Y for yes or N for no. "))
print("End of program. ")

#%%
#A short program to validate quiz score
quiz = float(input('Enter a quiz score between 0 to 10 : '))

#Validate the quiz score is between 0 and 10,
#loop until a valid score is entered
while quiz< 0 or quiz> 10:        
    print('The score you have entered is either negative or greater than 10.')        
    print('Please try again!')            
    quiz = float(input('Enter a quiz score between 0 to 10 : '))    #End of while block
print('The score is ', quiz)

#%% calculate amount due

price = float(input('Please enter the item price: $'))
# check to ensure the price entered is a valid number
while price < 0 :
    print("You cannot enter a negative price. Please try again. ")
    price = float(input('Please enter the item price: $'))
    
quantity = int(input("Please enter the quantity sold: "))
# check to ensure the quantity entered is a valid number
while quantity < 0 :
    print("Quantity sold must be positive. Please try again. ")
    quantity = int(input('Please enter the quantity sold: '))

#display the reatil price
total_price = price * quantity
print("The total price is $", total_price, sep = '')


#%% compute hourly rate bonus exercise

loop = 'y'
total_hourly_rate = 0
count = 0

while loop == "y":
    hourly_rate = float(input("Enter hourly rate: "))

    while hourly_rate < 10.00 or hourly_rate > 100.00:
        print("The hourly rate has to be between 10 and 100.")
        hourly_rate = float(input("Enter hourly rate: "))
    
    print("Your hourly rate is ", format(hourly_rate, '.2f'))
    total_hourly_rate += hourly_rate
    count += 1
    loop = input("Enter y to continue and any other character to quit: ")

average = total_hourly_rate/count
print("\n")
print("------Summary------")
print("The number of users who have entered their hourly rate is ", format(count, '.2f'))
print("The sum of the hourly rates is ", format(total_hourly_rate, '.2f'))
print("The average hourly rate is ", format(average, '.2f'))
   
#%%
# The For Loop
# count-controlled loop, iterates a specific # of times, Works with a sequence of items
# Iterates one time for each item in the sequence
# for variable in [value1, value2, etc.]

for num in [1, 2, 3, 4, 5]:
    print("num:", num)

for var in [1, 3, 5, 7]:
    square = var**2
    print("var:", var, "\tvarsquared:", square)

for name in ["Yan", "Yunyi"]:
    print("name:", name)
    
#%%  
num = 0
while num<5:
    print("I will pay attention in class")
    num += 1
    
for num in [0,1,2,3,4]:
    print("I will pay attention in class")
    
#%%  
# range(5)produces this sequence: [0, 1, 2, 3, 4]

for num in range(101):
    print(num)
    
for num in range(5):
    print("num:", num)    
#%%
for num in range(2, 8):            #starts at 2, ends at 7
    print("num:", num)
    
for num in range(10, 51):
    print(num)
#%%
    
for num in range(1, 10, 2):         #print odd
    print(num)

for num in range(1, 20, 3):         #print odd
    print("num:", num)
    
for num in range(2, 101, 2):        #print even from 1 - 100
    print("num:", num)
    
#%%   
# negative step values

for num in range(20, 0, -2):
    print("num:", num) 
    
    
#%%
# user controls the list

start = int(input("What is the starting value of the list? "))
end = int(input("What is the ending value of the list? "))
cnt = 0
total_sum = 0
product = 1

for num in range(start, end + 1):
    print(num)
    cnt += 1
    total_sum += num
    product *= num

average = total_sum/cnt
print("sum:", total_sum)
print("average:", format(average, '.2f'))
print("product:", format(product, '.0f'))

#%%

for row_number in range (3):    
    print('Row number ', row_number+1, ' :', end = ' ')           
    for column_number in range (5):        
        print(' ', column_number+1, end = ' ')            
    print() # indent this line and align it with print statement above, see the diff?


#%% averaging test scores

students = int(input("How many students do you have? "))
test_scores = int(input("How many test scores per student? "))

for student in range(students):
    print("Student number", student+1)
    print('-----------------')
    score_sum = 0
    for x in range(test_scores):
        print('Test number', x+1, end='')       
        score = float(input(': '))
        score_sum += score
    average = score_sum/test_scores
    print("\nThe average for student number", student+1, "is: ", format(average, '.1f'))

#%% fun practicing loops

for row in range(10):
    for column in range(8):
        print("*", end ='')
    print()
  

base_size = int(input("What is the base size? "))
for row in range(base_size):
    for column in range(row + 1):
        print("*", end = '')
    print()

top_size = 8
for row in range(top_size):
    for column in range(top_size - row):
        print("*", end = '')
    print()

#%%










