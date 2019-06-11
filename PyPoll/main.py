#import libraries
import os
import csv

#set path for csv file
csvpath = os.path.join("03-Python_Homework_PyPoll_Resources_election_data.csv")

#create list to store data
voter = []
vote = []
candidates = []

#open the csv file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # start from second row
    next(csvreader)
    # create a loop
    for row in csvreader:
    # add votes to list
        voter.append(row[0])
        vote.append(row[2])
    # create function to select unique values in vote
    def unique(list):
        
        for x in list:
            if x not in candidates:
                candidates.append(x)
    unique(vote)
    # thinking about maybe create a dictionary


#Result
    print('Election Result')
    print('-------------------------------------')
    #print('Total Votes: '+ str(len(voter)))
    print('-------------------------------------')
    print(candidates)
