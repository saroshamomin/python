#Author: Sarosha Momin
#Homework Number & Name: Audiobooks HW 2
#Due Date: Septemeber 17
#Program Description: gBooks, a subsidiary of Grapefruit Company, sells audiobooks.
# They have developed a program to incent customers to purchase many books at a time to increase sales.  
# They have also created a membership program to provide even better deals for their best customers.  
# Write a Python program that accepts information from the user (customer), calculates the price of the 
# books sold, and displays a receipt of this information to the customer.  You should assume that the tax 
# rate is 8.25%.


# create variables to store the inital info from the customer to use for calculations and product summary
name = str(input("What is your name? "))
number_of_books = int(input("How many books would you like to buy? "))
membership = str(input("What kind of member are you? Press R for Regular or P for Premium. "))
total_books = number_of_books
TAX_RATE = .0825            # storing the fixed tax rate 
membership_fee = 0.0        # creating this varaible to be used in the case that a regular member upgrades
upgrade = "y or n"

# asking the user if they would like to upgrade, and changing value of membership if they do
if membership == 'R':
    upgrade = str(input("Would you like to upgrade to a Premium membership for a fee of $4.95? Enter Y for Yes or N for No. "))
if upgrade == 'Y':
    membership = 'P'

# solving for how many total & free books the customer will receive as well as the book price based on membership type 
if membership == 'R':
    book_price = 9.95
    membership = "Regular"
    if number_of_books < 8:
        total_books = number_of_books
    if number_of_books >= 8 and number_of_books <= 12:
        total_books = number_of_books + 1
    if number_of_books > 12:
        total_books = number_of_books + 2
elif membership == 'P':
    book_price = 8.49
    membership = "Premium" 
    if number_of_books < 6:
        total_books = number_of_books
    if number_of_books >= 6 and number_of_books <= 9:
        total_books = number_of_books + 1
    if number_of_books > 9:
        total_books = number_of_books + 2
      
# calculating and printing the customers product summary based on the information collected above includin the tax, subtotal and total cost
print("\n")
print("-------------Product Summary-------------")
print("Customer Name:", name)
print("Customer Type:", membership)    
print("Total Books:", total_books)
subtotal = book_price * number_of_books
print("Subtotal: $", format(subtotal, '.02f'), sep ='')
if upgrade == 'Y':
    membership_fee = 4.95
    print("Thank you for upgrading to premium membership!")
    print("Membership Fee: $", membership_fee, sep = '')
tax = subtotal * TAX_RATE
print("Tax: $", format(tax, '.02f'), sep = '')
total_cost = subtotal + tax + membership_fee
print("Total: $", format(total_cost, '.02f'), sep = '')
