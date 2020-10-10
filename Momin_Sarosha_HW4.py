#Author: Sarosha Momin
#Homework Number & Name: Grade Calculator HW4
#Due Date: October 8
#Program Description: Create an application to determine a student’s numerical and letter grade in MIS 304.

#assigning the constants to variables
EXAM_WEIGHT = .20
HW_WEIGHT = .20
LANGQR_WEIGHT = .10
PROJ_WEIGHT = .10

#main function used to call getGrade(), calculate_grades(), and letter_grade() 
def main():
    assignment = "Exam 1"  #variable created to assign the name of each assignment used when calling get_grade() 
    exam1 = getGrade(assignment)
    assignment = "Exam 2"
    exam2 = getGrade(assignment)
    assignment = "Exam 3"
    exam3 = getGrade(assignment)
    assignment = "Homework"
    hw = getGrade(assignment)
    assignment = "Language Quick Reference"
    langqr = getGrade(assignment)
    assignment = "Final Project"
    project = getGrade(assignment)
    grade = calculate_grades(exam1,exam2,exam3,hw,langqr,project)  
    print("\nFinal Numeric Grade:", format(grade, '.2f'))
    letter = letter_grade(grade)                    
    print("Final Letter Grade:", letter) 
    
#takes input and ensures the grade is a valid number, loops until user enters a valid response 
def getGrade(assignment):
    try: 
        grade = float(input("What is your grade for " + assignment + "? "))
        while grade < 0 or grade > 100 : 
            print("Grade must be a number between 0 and 100.")
            grade = float(input("What is your grade for " + assignment + "? "))
    except ValueError:
        print("Grade must be a number between 0 and 100.")
        grade = float(input("What is your grade for " + assignment + "? "))
        while grade < 0 or grade > 100 : 
            print("Grade must be a number between 0 and 100.")
            grade = float(input("What is your grade for " + assignment + "? "))
    return grade          #returns the grades of each assignment

#takes the different grade values and calculates it using the weighted constants
def calculate_grades(exam1,exam2,exam3,hw,langqr,project):
    grade = (((exam1 + exam2 + exam3)/3) * (EXAM_WEIGHT * 3)) + (hw * HW_WEIGHT) + (langqr * LANGQR_WEIGHT) + (project * PROJ_WEIGHT)
    return grade

#function that will take the computed grade, assign it a letter value and return the letter
def letter_grade(grade):
    if grade >= 89.5:
        letter_grade = "A" 
    elif grade >= 79.5:
        letter_grade = "B"  
    elif grade >= 69.5:
        letter_grade = "C" 
    elif grade >= 59.5: 
        letter_grade = "D" 
    elif grade < 59.5:
        letter_grade = "F" 
    return letter_grade
        
main()

