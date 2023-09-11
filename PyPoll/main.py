#Modules
import os
import csv

#set path for file
election_data_csv = os.path.join('C:/Users/liam/OneDrive/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

total_votes = 0
candidates = {}
winner = ""
winner_count = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.DictReader(election_data_csv)
    
    for row in csvreader:
        
        total_votes += 1
        
        
print(total_votes)