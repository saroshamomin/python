#Author: Sarosha Momin
#Homework Number & Name: Stock Prices HW6
#Due Date: October 22
#Program Description: Take Apple's stock prices for the year and read it to a list. The list 
# should also have corresponding week, and changes from the previous week. If user asks for information,
# be able to display the average change, highest change and lowest change for the range of weeks. 

#append stock prices, week and change to a list. obtain input from user and use it for calculations/displays.
def main():
    apple_data = open('ApplePrices.txt', 'r')
    total = 0
    cnt = 1
    change = 0
    count = 0
    info = apple_data.readline().rstrip('\n')
    applelist = []
    while info != '':                             #read the file with Apple's stock prices and add to a list
        stockprice = float(info)
        applelist.append([cnt,format(stockprice, '.2f'),change])
        cnt += 1
        info = apple_data.readline()
    for x in range(1,52):
        change = float(applelist[x][1]) - float(applelist[x-1][1])
        applelist[x][2] = format(change, '.2f')
    startweek = int(valid_input('start'))
    endweek = int(valid_input('end'))
    minimum = 300
    maximum = -1
    for x in range(startweek-1, endweek):
        changes = float(applelist[x][2])     #calculate changes in stock price for a given range by the user
        total += changes            
        count += 1
        if changes < minimum:        #provide the minimum and maximum change in price for the range
            minimum = changes
            lowweek = x + 1
        if changes > maximum: 
            maximum = changes
            highweek = x + 1
    avg = total/count
    print("Start Week:", startweek)
    print("End Week:", endweek)
    print("The average change is", format(avg, '.2f'))
    print("The week with the highest change is week", highweek , "with a change of", maximum)
    print("The week with the lowest change is week", lowweek , "with a change of", minimum)

#ensure the user enters a valid input for the weeks
def valid_input(beg_end):  
    week = -1
    while week < 1 or week > 52:
        week = input("Enter the " + beg_end + " week: ") 
        try:
            if week == '' and beg_end == 'start':          #if the user chooses to leave blank, the start week should be 1
                week = 1                                   #and the end week should be 52
            elif week == '' and beg_end == 'end':          
                week = 52
            week = int(week)
        except Exception as err: 
            print(err)
            week = -1 
    return week
    
main()