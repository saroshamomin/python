#Author: Sarosha Momin
#Homework Number & Name: GradeBook HW5A
#Due Date: October 15
#Program Description: Display the names and grades of students in gradebook.txt. Also display the maximum and minimum grade.

#The max and min grade is calculated and displayed along with each student's name and grade.
def main():
    maximum = -1
    minimum = 101
    gradebook_file = open('gradebook.txt', 'r')
    student_info = gradebook_file.readline()
    while student_info != '':                  #loop until it goes through each student and their grades.
        grade = float(gradebook_file.readline())
        student_info = student_info.rstrip('\n')
        print(student_info, "'s grade is ", grade, sep = "")
        if minimum > grade:
            minimum = grade
        if maximum < grade:
            maximum = grade
        student_info = gradebook_file.readline()   
    print("The minimum is", minimum)
    print("The maximum is", maximum)    
    gradebook_file.close()
main()