#Program header goes here
#Define constants
DATA_FILE = "ContactInfo.txt"

VIEW_NAMES = 1
VIEW_ALL = 2
VIEW_SPECIFIC = 3
ADD_CONTACT = 4
REMOVE_CONTACT = 5
UPDATE_ADDR = 6
EXIT = 7

#Define main function
def main():
    #Create empty dictionaries
    street_dict = {}
    city_dict = {}
    zip_dict = {}

    #Load data from input file into dictionaries
    #YOU WILL NEED TO ADD LOGIC TO MAKE THIS FUNCTION WORK
    create_dictionaries(street_dict, city_dict, zip_dict)

    #DEBUGGING - Print the contents of each dictionary after you read the data from the
    #input file so that you know the data in each is correct
##    print("street_dict", street_dict)
##    print("city_dict", city_dict)
##    print("zip_dict", zip_dict)

    #Display menu for user
    print_menu()

    #Get user's choice
    menu = get_user_choice()

    #Loop through menu
    while menu != EXIT:
        if menu == VIEW_NAMES:
            #INSERT CODE HERE TO VIEW NAMES OF ALL CONTACTS
            print("View names of contacts.")

            #Name is the key, so the loop will grab each key and print it
            for name in street_dict:
                print(name)

        elif menu == VIEW_ALL:
            #INSERT CODE HERE TO VIEW CONTACT INFO FOR ALL CONTACTS
            print("View all contact info of each contact.")

            #Use the key (name) to get the values from each dictionary
            for name in street_dict:
                address = street_dict[name]
                city = city_dict[name]
                postal_code = zip_dict[name]

                #Call the function to display each contact's info nicely
                display_contact_info(name, address, city, postal_code)

        elif menu == VIEW_SPECIFIC:
            #Ask user for name of contact to view
            name = input("Whose contact information would you like to view? ")
            
            #Ensure that the person entered exists in the dictionary
            if name in street_dict:
                address = street_dict[name]
                city = city_dict[name]
                postal_code = zip_dict[name]

                #Display that person's contact info using this function
                display_contact_info(name, address, city, postal_code)
            else:
                print("Name not found.")

        elif menu == ADD_CONTACT:
            #Prompt user for new contact info
            name = input("What is the name of the new contact? ")
            address = input("What is the street address for " + name + "? ")
            city = input("In what city does " + name + " live? ")
            postal_code = input("What is the zip code? ")
            
            #Before adding the person to the dictionaries, make sure they don't
            #already exist in the dictionaries
            if name not in street_dict:
                street_dict[name] = address
                city_dict[name] = city
                zip_dict[name] = postal_code
            else:
                print("Contact exists. Can't add new one.")

        elif menu == REMOVE_CONTACT:
            #Prompt user for contact to remove
            name = input("Whose contact information would you like to delete? ")

            #INSERT CODE HERE TO REMOVE THE CONTACT
            if name in street_dict:
                del street_dict[name]
                del city_dict[name]
                del zip_dict[name]
            else:
                print(name, "does not exist to delete.")

        elif menu == UPDATE_ADDR:
            #Prompt user for contact to update
            name = input("Whose street address would you like to update? ")
            address = input("What is the street address for " + name + "? ")
            city = input("In what city does " + name + " live? ")
            postal_code = input("What is the zip code? ")

            #Make sure the person exists in the dictionary so that you are
            #changing that person's info and not adding a new person
            if name in street_dict:
                street_dict[name] = address
                city_dict[name] = city
                zip_dict[name] = postal_code
            else:
                print("Contact does not exist. Can't update.")
           
        #Get user's choice
        menu = get_user_choice()

#Define function to create dictionaries
def create_dictionaries(addr_dict, cities_dict, zips_dict):
    #Open input file
    contact_info_file = open(DATA_FILE, 'r')

    #Loop to read data from file and split line read from file
    for line in contact_info_file:
        #Remove \n from end of the line read from the file
        line = line.rstrip('\n')
        #Split the line read from the file into a list of string values
        line_list = line.split(":")
#        print('line_list', line_list)
        # for line_sub in line_list:
        #     print(line_sub)

        #Assign values from the list to temporary variables
        #This step is not required, BUT makes your code easier to read
        name = line_list[0]
        street = line_list[1]
        city = line_list[2]
        zip_code = line_list[3]

        #DEBUGGING - print each of the values split from the file to make
        #sure that you're storing each value in the correct variable
        # print("name", name)
        # print("street", street)
        # print("city", city)
        # print("zip_code", zip_code)

        #Add each value to the appropriate dictionary using name as the key
        addr_dict[name] = street
        cities_dict[name] = city
        zips_dict[name] = zip_code


    #Close input file
    contact_info_file.close()

    ##Do not return anything from this function
    ##Like lists, dictionaries are passed by reference

#Define function to display contact info nicely
def display_contact_info(contact_name, addr, city, zip_code):
    print(contact_name)
    print(addr)
    #print(city, ", ", zip_code, sep = "")
    
#Define function to get user's menu choice
def get_user_choice():

    #Prompt user
    choice = int(input("What would you like to do? "))

    #Validate user input
    while choice < VIEW_SPECIFIC and choice > EXIT:
        choice = int(input("Invalid menu option. Please select again: "))

    return choice

#Define menu function
def print_menu():
    print("Please select an option from the menu below:")
    print("1. View a list of all contact names.")
    print("2. View contact information for all contacts.")
    print("3. View contact information for a specific person.")
    print("4. Add a new contact")
    print("5. Remove an existing contact")
    print("6. Update address for an existing contact")
    print("7. Exit")

#Call main function
main()
