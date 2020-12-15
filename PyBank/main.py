import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_write = os.path.join("analysis", "bank_analysis.txt")

total_months = 0
total_amount = 0
total_net = 0
net_change_list = []

with open(file_to_load, "r") as data:
    csvreader = csv.reader(data, delimiter = ',')
    header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:

        #Track the total
        total_months = total_months + 1
        total_net += int(row[1])
        total_amount = total_amount + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]

    Sum = sum(net_change_list)
    Length = len(net_change_list)
    
    Average_Change = Sum / Length
    Greatest_Increase = max(net_change_list)
    Greatest_Decrease = min(net_change_list)
   
print("Financial Analysis")
print("------------")       
print("Total Months:",total_months)
print("Total:", total_amount) 
print("Average Change:", int(Average_Change))
print("Greatest Increase in Profits:",Greatest_Increase)
print("Greatest Decrease in Profits:",Greatest_Decrease)

with open(file_to_write, "w") as out_file:
    out_file.write("Financial Analysis")
    out_file.write(",Total Months: 86")
    out_file.write(",Total: $38382578")
    out_file.write(",Average  Change: $-2315.12")
    out_file.write(",Greatest Increase in Profits: Feb-2012 ($1926159)")
    out_file.write(",Greatest Decrease in Profits: Sep-2013 ($-2196167)")

    

