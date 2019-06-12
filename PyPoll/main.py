#import libraries
import os
import csv

#set path for csv file
csvpath = os.path.join("03-Python_Homework_PyPoll_Resources_election_data.csv")

#create list to store data
voter = []
vote = []
candidates = []
candidate1 = []
candidate2 = []
candidate3 = []
candidate4 = []

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
    # create function to select unique values in vote and add it to candidate list
    def unique(list):
        
        for x in list:
            if x not in candidates:
                candidates.append(x)
    #run function
    unique(vote)
    #find number of votes for each candidate
    for x in vote:
        if x == candidates[0]:
            candidate1.append(x)
        if x == candidates[1]:
            candidate2.append(x)
        if x == candidates[2]:
            candidate3.append(x)
        if x == candidates[3]:
            candidate4.append(x)
    #calculate percentages
    percent1 = round(int(len(candidate1))/int(len(vote))*100,1)
    percent2 = round(int(len(candidate2))/int(len(vote))*100,1)
    percent3 = round(int(len(candidate3))/int(len(vote))*100,1)
    percent4 = round(int(len(candidate4))/int(len(vote))*100,1)
    #create a function to find the winner candidate
    def winner(list):
        return max(set(list), key = list.count)
    



#Result
    print('Election Result')
    print('-------------------------------------')
    print('Total Votes: '+ str(len(voter)))
    print('-------------------------------------')
    print(candidates[0]+": "+ str(percent1) +"% ("+str(len(candidate1))+")")
    print(candidates[1]+": "+ str(percent2) +"% ("+str(len(candidate2))+")")
    print(candidates[2]+": "+ str(percent3) +"% ("+str(len(candidate3))+")")
    print(candidates[3]+": "+ str(percent4) +"% ("+str(len(candidate4))+")")
    print('-------------------------------------')
    print("Winner :"+winner(vote))
