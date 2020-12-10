import os
import csv


poll_data = os.path.join('Resources','election_data.csv')

with open(poll_data, "r") as pollfile:
    pollreader = csv.reader(pollfile, delimiter = ",") 
    
    next(pollreader,None)
    Voters = []
    County = []
    Candidates = []
    Number_votes = 0

    for row in pollreader:
        Voters.append(row[0])
        County.append(row[1])
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Number_votes = Number_votes + 1

print (Candidates,Number_votes)

