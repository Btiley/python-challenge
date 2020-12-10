import os
import csv


bank_data = os.path.join('Resources','budget_data.csv')

with open(bank_data, "r") as bankfile:
    bankreader = csv.reader(bankfile, delimiter = ",") 
    
    #Skip header row
    next(bankreader,None)
    rev = []
    date = []
    total = 0
    
 
    
    for row in bankreader:
        Profit_Loss = rev.append(row[1])
        date.append(row[0])
       
        total_dates = len(date)
        total += int(row[1])
        
        min = min(Profit_Loss)
        max = max(Profit_Loss)
    print(max, min)
    average_total = total/total_dates

    print("Number of Dates :", total_dates)
    print("Net Profit/Loss :", total)
    print("Average Profit/Loss :", average_total)

 
 

    

    













    
    #Select Profit/Losses Row
    #Get net total
    #Get Average
    #Get Max value
    #Get min value
    
    #Converts CSV data into a list 
    #lines = bankfile.readlines()
    #number_dates = len(lines)
    #print('Number of dates: ', number_dates)
    

    #Print Sum of Profit/Losses Column
    #total = 0
    # 
        #total += int(row[1])
    #print(total)
    


