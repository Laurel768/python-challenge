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

# open csv file, separate data with commas
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip header row
    csv_header = next(csvreader)
#calculate number of months, change in profit or loss
    for row in csvreader:
        total_months += 1
        total_profit_or_loss +=int(row[1])
        if total_months > 1:
            month_change_profit_or_loss = int(row[1]) - prior_month_change_profit_or_loss

        total_month_change += month_change_profit_or_loss 

        prior_month_change_profit_or_loss = int(row[1]) 
      
        if month_change_profit_or_loss > greatest_increase:
            greatest_increase = month_change_profit_or_loss
            greatest_increase_month = row[0]

        if month_change_profit_or_loss < greatest_decrease:
            greatest_decrease = month_change_profit_or_loss
            greatest_decrease_month = row[0]
            
# had to move this down to bottom, outside of "for" statement

average_change = total_month_change /(total_months - 1)         
 # to print on screen   
print ("Financial Analysis")
print ("----------------------------")
print("Total Months: " +str(total_months))
print("Total: $" + str(total_profit_or_loss))
print("Average Change: $" + str(format(average_change, ".2f")))
print("Greatest increase in profits: " + greatest_increase_month + " ($" + str(greatest_increase) +")")
print("Greatest decrease in profits: " + (greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")
# to print to file
f = open("analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write("Total Months: " +str(total_months) + "\n")
f.write("Total: $" + str(total_profit_or_loss ) + "\n")
f.write("Average Change: $" + str(format(average_change, ".2f")) + "\n")
f.write("Greatest increase in profits: " + greatest_increase_month + " ($" + str(greatest_increase) +") \n")
f.write("Greatest decrease in profits: " + (greatest_decrease_month) + " ($" + str(greatest_decrease) + ") \n")
f.close()
