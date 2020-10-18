#Author: Sarosha Momin
#Program Description: Allow the user to edit a student's grade in gradebook.txt and update the file.

from Momin_Sarosha_HW5_Functions import valid_avg
import os

#use loops to parse through the file and search for the student's name and update their grade
def main():
    gradebook_file = open('gradebook.txt', 'r')
    temp_file = open('temp.txt', 'w')                  #create new file to store the edited information
    found = False
    find_name = input("What student do you want to find? ")
    student_info = gradebook_file.readline() 
    while student_info != '':
        grade = float(gradebook_file.readline())
        student_info = student_info.rstrip('\n')
        if student_info == find_name:
            new_grade = valid_avg()
            temp_file.write(student_info + '\n')
            temp_file.write(str(new_grade) + '\n')
            found = True
        else:
            temp_file.write(student_info + '\n') 
            temp_file.write(str(grade) + '\n')
        student_info = gradebook_file.readline()
    gradebook_file.close()
    temp_file.close()
    os.remove('gradebook.txt')               #remove original file and replace it with the updated temp file
    os.rename('temp.txt', 'gradebook.txt')
    if found:
        print("The student's grade has been updated.")
    else:
        print('That student was not found in the file.')        
main()
