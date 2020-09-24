# Author: Sarosha Momin

#Program Description: A local store wants to identify which face mask have the highest profit margin and 
# are the most popular. They have hired you to update some of their systems.  Your first task is to create 
# an application to record the sales and calculate profit for individual masks sold.  Write a program that 
# accepts information from the user (a store clerk), calculates the total selling price, cost, and profit, 
# and displays a summary of the item sold.



# Information entered by the user including the product’s name, price, cost and quanitity
product_name = str(input("What is the name of the item being sold? "))
price = float(input("What is the price of the item being sold? "))
cost = float(input("What is the cost of the item being sold? "))
quantity = int(input("How many of the items were sold? "))
print("\n")

# Create variables to solve for total revenue, total cost, and total profit in % and $
revenue = price * quantity
total_cost = cost * quantity
profit = revenue - total_cost
percent_profit = int((profit/revenue) * 100)



# Output the product name, total revenue, total cost, quantity sold, total profit in $ and %
# format revenue, total cost, and profit so that they are outputted with two decimals
print("Item Name:", product_name)
print("Total Revenue: $", format(revenue, '.02f'), sep='')
print("Total Cost: $", format(total_cost, '.02f'), sep='')
print("Quantity Sold:", quantity)
print("Total Profit: $", format(profit, '.02f'), sep='')
print("Percentage of Profit: ", percent_profit, "%", sep='')


