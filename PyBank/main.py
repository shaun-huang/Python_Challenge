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
amount_2 = []
amount_change = []

#open the csv file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # add months and amount to list from the second row
    next(csvreader)
    for row in csvreader:
        month.append(row[0])
        amount.append(int(row[1]))
    # add the monthly amount change
        amount_2.append(int(row[1]))
    # get amount iteration's value
    amount_2.pop(0)
    #Generate Report
    print("Financial Analysis")
    print("-----------------------------------")
    # determine total months
    print("Total Month: " + str(len(month)))
    # determine net amount within the period
    print("Total Amount: "+ str(sum(amount)))
    # determine average change
    print(amount_change)

