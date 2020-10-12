#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:01:01 2020

@author: saroshamomin
"""

grades_file= open('Grades.txt', 'w')

SALES_FILE = 'Sales.txt'
sales_data= open(SALES_FILE, 'r')

REVENUE_FILE = 'Revenue.txt'
revenue_data= open(REVENUE_FILE, 'a')

grades_file.close()
sales_data.close()

#Read the entire contents of a file
variable = SALES_FILE.read()

#Read a single line of a file
variable = grades_file.readline()

#%%

student_data = open('Documents/studentNames.txt', 'r')
for student in range(3):
    name = student_data.readline()
    print("Student name:", name)
student_data.close() 

#%% read file with unknown number of lines

def main():        
    student_data = open('Documents/studentNames.txt','r')    
    student = student_data.readline() 
    while student != '':        
        print('Student name:', student)        
        student = student_data.readline()    
    student_data.close()
    
main()
    
#%%

student_data = open('Documents/studentNames.txt', 'r')
for student in student_data:          #Automatically reads a line in a file and stores it in student
    name = student.rstrip('\n')     #Removes the trailing \n from the line read from the file
    print("Student name:", name)
    student_data.close()
    
#%%

cnt = 0
student_data = open('Documents/studentNames.txt','r')    
student = student_data.readline() 
while student != '':
    name = student.rstrip('\n')         
    print('Student name:', name)        
    student = student_data.readline()  
    cnt += 1
student_data.close()

print(cnt, "students in the file")

#%%

def main():
    class_data = open('ClassList.txt', 'w')
    for classes in range(3):
        class_name= input("Please enter a class (e.g. MIS 304): ")
        class_data.write(class_name + "\n")
    class_data.close()
    
main()

#%%

def main():
    class_data = open('ClassList.txt', 'w')
    for classes in range(3):
        class_name = input("Please enter a class (e.g. MIS 304): ")
        class_data.write(class_name + "\n")
    class_data.close()

main()

#%%

student_file = open('Documents/studentNames.txt', 'r')
StudentsandGrade = open('studentandgrades.txt','w')  
while student != '':
    student = student_file.readline()
    name = student.rstrip('\n') 
    grade = input("Please enter the grade for " + student + ': ')
    StudentsandGrade.write(student + grade + "\n")
StudentsandGrade.close()

#%%

file_variable = open(file_name,'r')
first_line = file_variable.readline()
while first_line!= '':
    field_1= file_variable.readline()
    field_2= file_variable.readline()
    first_line= file_variable.readline()
    
file_variable.close()


#%%

city_data = open('CityProfit.txt', 'r')
city_name = city_data.readline().rstrip('\n')
while city_name!= '':
    q1_profit = float(city_data.readline())
    q2_profit = float(city_data.readline())
    q3_profit = float(city_data.readline())
    tot_profit= q1_profit + q2_profit + q3_profit
    print(city_name, " profit is $", tot_profit, sep="")
    city_name= city_data.readline().rstrip('\n')
    
city_data.close()


#%%

student_info = open('Documents/studentsAndGrades.txt', 'r')
student_name = student_info.readline().rstrip('\n')
total_grade = 0
total_students = 0

while student_name!= '':
    grade = float(student_info.readline().rstrip('\n'))
    total_grade += grade
    total_students +=1
    print(student_name, "'s grade is ", grade, sep="")
    student_name= student_info.readline().rstrip('\n')

avg = total_grade / total_students
print("The average is", format(avg, '.2f'))
student_info.close()


#%%

def main():    
    try:        
        num1 = int(input("Enter a number: "))            
        num2 = int(input("Enter another number: "))  #try typing in zero                
        quotient = num1 / num2        
        print(num1, "divided by", num2, 'is', quotient)            
    except:        
        print ("Exception handling section: You cannot divide by zero")        
        
main()


#%%

