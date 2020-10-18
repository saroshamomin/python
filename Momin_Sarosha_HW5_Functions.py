#Author: Sarosha Momin
#Homework Number & Name: GradeBook HW5 (Functions)
#Due Date: October 15
#Program Description: create functions that can be imported in different files

#prompts user for student name and makes sure its a valid name
def valid_name():
    name = str(input("Enter the name: "))
    while len(name) <= 1 or name.isalpha() == False or name.isdigit():
        print("That is not a vaild name. Please try again.")
        name = str(input("Enter the name: "))
    return name

#prompts user for student's average and validates the score 
def valid_avg():
    loop = 'yes'
    while loop  == 'yes':
        try:
            avg = float(input("Enter the average: "))
            while avg < 0 or avg > 100:
                print("That is not a vaild average. Please try again.")
                avg = float(input("Enter the average: "))
            loop = 'no'
        except Exception as err:
            print(err)
    return avg