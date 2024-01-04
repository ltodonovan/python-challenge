#Modules
import os
import csv

#set path for file
election_data_csv = os.path.join('C:/Users/liam/OneDrive/Desktop/python-challenge/python-challenge/PyPoll/Resources/election_data.csv')

total_votes = 0
candidates = {}
winner = ""
winner_count = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        #calculate total votes
        total_votes += 1
        #get candidates name
        candidate = row["Candidate"]
        #get candidates vote counts
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    #find candidate winner
    for candidate, votes in candidates.items():
        if votes > winner_count:
            winner = candidate
            winner_count = votes
            
#create analysis of election result data
analysis = f"Election Results\n" \
f"----------------------------\n" \
f"Total Votes: {total_votes}\n" \
f"----------------------------\n" 
for candidate, votes in candidates.items():
    candidate_votes = (votes / total_votes) * 100
    analysis += f"{candidate}: {candidate_votes:.3f} % ({votes})\n"
analysis += f"----------------------------\n" \
f"Winner: {winner}\n" \
f"----------------------------\n"

print(analysis)

#output the analysis results
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as file:
    file.write(analysis)