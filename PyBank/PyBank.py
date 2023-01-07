import os
import csv

#set path for file
csvpath = os.path.join ("Resources", "budget_data.csv")
outpath = os.path.join ("analysis", "budget_analysis.txt")

total_profit =0

total_month =0 
months_of_change =0
pre_profit =0
current_profit =0
total_change =0
greatest_increase =0
greatest_decrease =0
greatest_increase_date =""
greatest_decrease_date =""

#open and read the csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')

    next(csv_reader)

    for row in csv_reader:
        #print(row)
        #exit()
        total_month +=1
        total_profit = total_profit + int(row[1])
        
        current_profit = int(row[1])
        change =0
    

        if pre_profit != 0: 
            change = current_profit - pre_profit 
            total_change += change
            months_of_change +=1

        pre_profit = current_profit 

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]

        
            


print(f"\nThe_outcome_is: {total_profit}\n" )

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit:,}
Average Change: ${total_change/months_of_change:,.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,.2f})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,.2f})
"""

print(output)

with open(outpath, "w") as out_file:  
    out_file.write(output)


     
