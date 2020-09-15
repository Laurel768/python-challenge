# Importing the os and csv module to create file paths across operating systems
import os
import csv

# Resources is in same folder as main.py, so we don't need to go anywhere to get it("..")
# budget_data is our csvpath
#csv_file = os.path.join("folder_name", "file.csv")
csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profit_or_loss = 0
average_change = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        total_profit_or_loss +=int(row[1])
        average_change = total_profit_or_loss/total_months



 
print ("Financial Analysis")
print ("----------------------------")
print("Total Months: " +str(total_months))
print("Total: $" + str(total_profit_or_loss))
print("Average Change: $" + str(average_change))





