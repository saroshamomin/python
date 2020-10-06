#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:13:04 2020

@author: saroshamomin
"""
#%%
def print_greeting():
    print("Hello MIS 304!")
    print("Today we will learn about functions.")

print_greeting()

def print_message():
    print("Hello World!") 
print_message()

#%%

#First define the main function
def main():
    print("Hello world (main)")
    print_name()
    print("Back in main")

# Next define the print_name function
def print_name():
    name = "Sarosha"
    print("Hello", name)
    
# Call the main function
main()
#%%

def main():
    message = "Hello MIS 304"
    print_message(message) # message is the argument
    print(message)
    
# Next define the print_message function
def print_message(msg_to_display): # msg_to_display is the parameter
    print(msg_to_display)
    msg_to_display = "The end"

# Call the main function 
main()

#%%

def main():
    number = int(input("Please enter an integer: "))
    getSquare(number)
    print("Program complete.")
        
def getSquare(num):
    square = num ** 2
    print("The square of", num, "is", square, end = '.\n')
    
main()
#%%

inputStr = input("Enter input: ")  #enter two binary nums with comma
inputStr = inputStr.split(",")
sum = int(inputStr[0], 2) + int(inputStr[1],2)
result = bin(sum)
result = result[2:]
print("Output is:",result)

#%%

# First define the main function
def main():
    num = 10.0
    change_number(num) # num is the argument
    print(num)
    
# Next define the change_number function
def change_number(number_to_change): # number_to_changeis the parameter
    print(number_to_change)
    number_to_change= 20
    print(number_to_change) # Call the main function
    
main()

#%%

def get_number():
    number = int(input("Please enter a number: "))
    return number

def calculate_square(value):
    square = value ** 2
    return square

num = get_number()
num_square = calculate_square(num)

#%%

def main():
    number1= 5   # local variable in main()    
    number2= 2   # local variable in main()    
    result = subtract2numbers(number1, number2)  #value returned is stored in result    
    print('In main, the result is ', result)
    
def subtract2numbers(num1, num2):   # num1 and num2 are parameters    
    difference = num1 -num2  #local variable inside the function        
    return difference

main()
#%%
DISC_PERCENTAGE = .20
def main():
    cost = getPrice()
    final_price = cost - calculateDiscount(cost)
    print("Final Price: $",format(final_price, '.2f'), sep = '')
    
def getPrice():          
    price = float(input("What is the original price? "))
    return price 

def calculateDiscount(price):
    discount = price * DISC_PERCENTAGE
    return discount
    
main()
#%%

multiple = 5
def main():
    number = int(input("Please enter a number: "))
    new_number= calculate_multiple(number)
    print("New number:", new_number)
    
def calculate_multiple(value):
    new_value= value * multiple
    return new_value

main()
#%% 
value = 100
def main():
    global value 
    print("Value:", value)
    value = 10
    print_value()

def print_value():
    print("Value:", value)
    
main()
#%%

import random 
number = random.randint(1, 100)
print(number)

import math 
sqrt_num= math.sqrt(number)
print(sqrt_num)
#%% 

def main():
    num1 = 10
    num2 = 20
    num1, num2 = changenumber(num1,num2)
    print(num1, num2)
    
def changenumber(value1, value2):
    print(value1,value2)
    value3 = value1
    value1 = value2
    value2 = value3
    return value1, value2

main()
#%% write two functions that compute and print out the product of two numbers
def main():
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    product = getProduct(num1, num2)
    print("The product is", product)
    
def getProduct(value1,value2):
    product = value1 * value2
    return product
    
main()
#%% 
def main():
    firstname = str(input("What is your first name? "))
    lastname = str(input("What is your last name? "))
    first, last = reverse_order(firstname,lastname)
    print("Your name reversed is", firstname, lastname)
    
def reverse_order(first, last):
    name3 = first
    first = last
    last = name3
    return first, last

main()
#%%
def main():
    firstname = str(input("What is your first name? "))
    lastname = str(input("What is your last name? "))
    print("Your name reversed is")
    reverseorder(last=lastname,first=firstname)
    
def reverseorder(first, last):
    print(last,first)

main()

#%%






