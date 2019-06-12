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
amount1 = []
amount2 = []
amount_change = []

#open the csv file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # add months and amount to list from the second row
    next(csvreader)
    for row in csvreader:
        month.append(row[0])
        amount.append(int(row[1]))
    #find amount change between each months
        amount1.append(int(row[1]))
        amount2.append(int(row[1]))
    amount1 = amount[:-1]
    amount2.pop(0)
    amount_change = [x2 - x1 for (x1,x2) in zip(amount1,amount2)]
    #find average amount change
    average_change = round(sum(amount_change)/len(amount_change),2)
    #find greatest increase and decrease/Maybe create a dictionary here
        

    #Generate Report
    print("Financial Analysis")
    print("-----------------------------------")
    # determine total months
    print("Total Month: " + str(len(month)))
    # determine net amount within the period
    print("Total Amount: "+ str(sum(amount)))
    # determine average change
    print("Average Change: $"+ str(average_change))

