# Importing the os and csv module to create file paths across operating systems
import os
import csv

#csv_file = os.path.join("folder_name", "file.csv")
csvpath = os.path.join("Resources", "budget_data.csv")

# define variables as integers
total_months = 0
total_profit_or_loss = 0
month_change_profit_or_loss = 0
prior_month_change_profit_or_loss = 0
total_month_change = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

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
   
    # HOW DO I GET TOTAL_MONTHS TO BE ONE LESS?  86 - 1 = 85
        average_change = total_month_change / 85

     


        if month_change_profit_or_loss > greatest_increase:
            greatest_increase = month_change_profit_or_loss
            greatest_increase_month = row[0]

        if month_change_profit_or_loss < greatest_decrease:
            greatest_decrease = month_change_profit_or_loss
            greatest_decrease_month = row[0]
  
 
 
print ("Financial Analysis")
print ("----------------------------")
print("Total Months: " +str(total_months))
print("Total: $" + str(total_profit_or_loss))
print("Average Change: $" + str(format(average_change, ".2f")))
print("Greatest increase in profits: " + greatest_increase_month + " ($" + str(greatest_increase) +")")
print("Greatest decrease in profits: " + (greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")