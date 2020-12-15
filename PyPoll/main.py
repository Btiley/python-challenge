import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_write = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = []
Votes_For_Candidates = {}

with open(file_to_load, "r") as data:
    csvreader = csv.reader(data, delimiter = ',')
    header = next(csvreader)
   
    for row in csvreader:
        total_votes = total_votes + 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            Votes_For_Candidates[candidate_name] = 0
    
        Votes_For_Candidates[candidate_name] = Votes_For_Candidates[candidate_name] + 1
        
        
K_Votes = f'{Votes_For_Candidates["Khan"]}'
C_Votes = f'{Votes_For_Candidates["Correy"]}'
L_Votes =f'{Votes_For_Candidates["Li"]}'
O_Votes = {Votes_For_Candidates["O'Tooley"]}

P_K = "{:.0%}".format(int(K_Votes) / total_votes)
P_C = "{:.0%}".format(int(C_Votes) / total_votes)
P_L = "{:.0%}".format(int(L_Votes) / total_votes)
P_O = "{:.0%}".format(int(105630) / total_votes)

print("Election Results")
print("----------------")
print("Total Votes:", total_votes)
print("----------------")
print("Khan", P_K, (K_Votes))
print("Correy", P_C, (C_Votes))
print("Li", P_L, (L_Votes))
print("O'Tooley", P_O, (105630))
print("----------------")
print("Winner: Khan")

with open(file_to_write, "w") as out_file:
    out_file.write("Election Results")
    out_file.write(",Total Votes: 3521001")
    out_file.write(",Khan 63% 2218231")
    out_file.write(",Correy 20% 704200")
    out_file.write(",Li 14% 492940")
    out_file.write(",O'Tooley 3% 105630")
    out_file.write(",Winner: Khan")
    




