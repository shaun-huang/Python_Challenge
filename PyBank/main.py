# Financial Analysis
#-------------------------------------------------------------------------
# import libraries
import os
import csv

#set path for csv file
csvpath = os.path.join("03-Python_Homework_PyBank_Resources_budget_data.csv")

# create lists to store data
month = []
amount = []

#open the csv file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter",")
    # add months and amount to list
    for row in csvreader:
        month.append(row[0])
    for row in csvreader:
        amount.append(row[1])
    # determine total months
    



