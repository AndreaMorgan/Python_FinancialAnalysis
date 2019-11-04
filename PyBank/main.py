#Importing necessary libraries
import csv
import os

#Locating and reading csv source file
currentDir = os.getcwd()
#print(currentDir)
data = '../Python/Resources/budget_data.csv'

#Create two lists and populate them with column data
months = []
profit = []

with open(data, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter = ',')
    headers = next(csvread)
    #print(f'Headers {headers}')

    for i in csvread:
        months.append(i[0])
        profit.append(int(i[1]))

#Calculating the number of months and the total net profit over entire period
numMonths = len(months)

net_total = sum(profit)

#Creating a new list to calculate the monthly change in profit/loss 
monthly_net = []

for i in range(len(profit) - 1):
    change = profit[i + 1] - profit[i]
    monthly_net.append(change)

#Calculating the average monthly change in profit/loss over entire period
avgMonChg = (sum(monthly_net))/(len(monthly_net))

#Equalizing the length of monthly_net and months to correspond to correct period
monthly_net.insert(0, 0)
    
#Set variables for max and min profit/loss changes
maxAmt = max(monthly_net)
minAmt = min(monthly_net)

#Find the maximum change in the list and corresponding period
for i in range(len(monthly_net)):
    for i in range(len(months)):
        if monthly_net[i] == maxAmt:
            greatest = monthly_net[i]  
            greatMon = months[i] 

#Find the minimum change in the list and corresponding period
for i in range(len(monthly_net)):
        for i in range(len(months)):
            if monthly_net[i] == minAmt:
                least = monthly_net[i]  
                leastMon = months[i] 

#Printing the Analysis in console
print('Financial Analysis')
print('-----------------------------------------')
print(f'Total Months: {numMonths}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(avgMonChg, 2)}')
print(f'Greatest Increase in Profits: {greatMon} (${greatest})')
print(f'Greatest Decrease in Profits: {leastMon} (${least})')


#Write to a text file
with open('../Python/Resources/financial_analysis.txt', "w", newline ='\n') as textfile:
    textfile.write('Financial Analysis \n') 
    textfile.write('-----------------------------------------\n')
    textfile.write(f'Total Months: {numMonths} \n')
    textfile.write(f'Total: ${net_total} \n')
    textfile.write(f'Average Change: ${round(avgMonChg, 2)} \n')
    textfile.write(f'Greatest Increase in Profits: {greatMon} (${greatest}) \n')
    textfile.write(f'Greatest Decrease in Profits: {leastMon} (${least}) \n')


    

    


