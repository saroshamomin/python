#Author: Sarosha Momin

#Program Description: Create an application to compute retirement account balances. 


#receiving annual savings from the user  
annual_svng = float(input("What is your annual savings amount? "))
while annual_svng <= 0 :          #making sure it's a positive number inputed through conditions
    print("Please enter a positive number. ")
    annual_svng = float(input("What is your annual savings amount? "))
   
#receiving year to start saving from the user
start_svng = int(input("What year do you want to start saving? "))
while start_svng < 2020 or start_svng > 2100:         #making sure it's a valid input through conditions
    print("The year must be in between 2020 and 2100. Please try again. ")
    start_svng = int(input("What year do you want to start saving? "))

#receiving year to stop saving from the user  
stop_svng = int(input("What year do you want to stop saving? "))
while stop_svng < start_svng or stop_svng > 2100 or stop_svng < 2020 :       #making sure it's a valid input through conditions 
    print("The year must be in between 2020 and 2100 and greater than or equal to the start year. Please try again. ")
    stop_svng = int(input("What year do you want to stop saving? "))

#receiving year to retire from the user 
retire = int(input("What year do you want to retire? "))
while retire < stop_svng or retire > 2100 or retire < 2020:     #making sure it's a valid input through conditions 
    print("The year must be in between 2020 and 2100 and greater than or equal to the end year. Please try again. ")
    retire = int(input("What year do you want to retire? "))

#receiving interest rate from the user 
INTEREST_RATE = float(input("What is your interest rate? "))
while INTEREST_RATE < 1 or INTEREST_RATE > 15:       #making sure it's between 1 and 15 through conditions
    print("The interest rate must be between 1% and 15%. Please try again. ")
    INTEREST_RATE = float(input("What is your interest rate? "))
    
total_svngs = 0      #creating accumulator variable for the for loop
print("\nYear        Savings        Interests        Total") 
print("-----------------------------------------------------------")

# creating a foor loop to calculate the savings, interests and total savings based on the year
for year in range (start_svng, retire+1):
    if year <= stop_svng:             #before retirement
        add_svngs = annual_svng
    if year > stop_svng:             #after retirement
        add_svngs = 0
    intrst_earned = (total_svngs + add_svngs) * (INTEREST_RATE/100)    #calculating interest rate
    total_svngs = total_svngs + add_svngs + intrst_earned      #calculating total savings
    for column in range(1):
        print(year, "\t", format(add_svngs, '8,.0f'),"\t", format(intrst_earned, '12,.0f'), "\t", format(total_svngs, '12,.0f'))
        
