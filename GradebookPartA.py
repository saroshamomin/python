#Author: Sarosha Momin
#Program Description: Gather students' names and grades. Validate the input and append it to a file. 

from Momin_Sarosha_HW5_Functions import valid_name, valid_avg

#reference valid_name() and valid_avg() functions to get input from user, add the data to the file
def main():
    gradebook_data = open('gradebook.txt', 'a')
    keepgoing = 'y'
    total = 0
    while keepgoing == 'y' or keepgoing == 'Y':   #continue the loop until the user is done
        name = valid_name()
        avg = valid_avg()
        gradebook_data.write(name + '\n' + str(avg) + '\n')
        total += 1
        keepgoing = str(input("Do you want to add another student? (y for yes or any other key to stop): "))
    gradebook_data.close()
    print("\nThere were", total, "students added to the file.")
main()
