# Financial Analysis
#-------------------------------------------------------------------------
# import libraries
import os
import csv

#set path for csv file
csvpath = os.path.join("03-Python_Homework_PyBank_Resources_budget_data.csv")

# open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


