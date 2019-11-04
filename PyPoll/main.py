#Importing necessary libraries
import csv
import os

#Locating and reading csv source file
currentDir = os.getcwd()
#print(currentDir)
data = '../Python_Challenge/Resources/election_data.csv'

#Create lists, dictionary and populate them with column data

voter_id = []
candidates = []
totals = {}

#Open CSV file, read data and append values to lists, dictionary
with open(data, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter = ',')
    headers = next(csvread)
    #print(f'Headers {headers}')

    for i in csvread:
        voter_id.append(i[0])
        if i[2] not in candidates:
            candidates.append(i[2])
            totals[i[2]] = 1
        elif i[2] in candidates:
            totals[i[2]] += 1

#Calculate the total number of votes, and the max value in dictionary "totals"
total_votes = (len(voter_id))
winner = max(totals, key = totals.get)

#Print results to the terminal
print(" \nElection Results \n")
print("----------------------------------- \n")
print(f"Total Votes: {total_votes} \n")
print("----------------------------------- \n")  
for key, value in totals.items():
    print(f'{key} : {round((((value)/(total_votes))*100), 2)}% ({value})')
print("----------------------------------- \n")
print(winner)  
print("----------------------------------- \n")

#Print results to a textfile
with open('../Python_Challenge/Resources/election_analysis.txt', "w", newline ='\n') as textfile:
    textfile.write(" \nElection Results \n")
    textfile.write("----------------------------------- \n")
    textfile.write(f"Total Votes: {total_votes} \n")
    textfile.write("----------------------------------- \n")  
    for key, value in totals.items():
        textfile.write(f'{key} : {round((((value)/(total_votes))*100), 2)}% ({value}) \n')
    textfile.write("----------------------------------- \n")
    textfile.write(f'{winner} \n')  
    textfile.write("----------------------------------- \n")