#Modules
import os
import csv



#set path for file
budget_data_csv = os.path.join('C:/Users/liam/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

#store data
total_months = 0
total_revenue = 0
average_change = 0
previous_revenue = 0
total_change = []
revenue_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

with open(budget_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        #total month calculation
        total_months += 1
        #total revenue calculation
        total_revenue = total_revenue + int(row["Profit/Losses"])
        #average revenue calculation
        total_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change = revenue_change + [total_change]
        #greatest increase
        if total_change > greatest_increase[1]:
            greatest_increase[1] = total_change
            greatest_increase[0] = row["Date"]
        #greatest decrease
        if total_change < greatest_decrease[1]:
            greatest_decrease[1] = total_change
            greatest_decrease[0] = row["Date"]
    #averag_change    
    average_change = sum(revenue_change) / len(revenue_change)
        
        
#create financial analysis
analysis = f"Financial Analysis\n" \
f"----------------------------\n" \
f"Total Months: {total_months}\n" \
f"Total: ${total_revenue}\n" \
f"Average Change: ${average_change}\n" \
f"Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})\n" \
f"Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})"

print(analysis)

output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as file:
    file.write(analysis)
                          