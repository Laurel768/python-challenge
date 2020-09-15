# Importing the os and csv module to create file paths across operating systems
import os
import csv

# Resources is in same folder as main.py, so we don't need to go anywhere to get it("..")
# budget_data is our csvpath
#csv_file = os.path.join("folder_name", "file.csv")
csvpath = os.path.join("Resources", "budget_data.csv")

# define variables as integers
total_months = 0
total_profit_or_loss = 0
change_in_profit_or_loss = 0
prior_month__change_profit_or_loss = 0
total_change_in_profit_or_loss = 0
average_change = 0
month_change_profit_or_loss = 0
total_month_change = 0
average_months = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        total_profit_or_loss +=int(row[1])
        if total_months > 1:
            month_change_profit_or_loss = int(row[1]) - prior_month_change_profit_or_loss

        total_month_change += month_change_profit_or_loss 

        prior_month_change_profit_or_loss = int(row[1])

        average_change = total_month_change / total_months
  

       


 
print ("Financial Analysis")
print ("----------------------------")
print("Total Months: " +str(total_months))
print("Total: $" + str(total_profit_or_loss))
print(total_month_change)
print(average_change)
print(average_months)
print("Greatest increase in profits: $")
print("Greatest decrease in profits: $")






