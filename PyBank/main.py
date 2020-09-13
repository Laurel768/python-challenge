# Importing the os and csv module to create file paths across operating systems
import os
import csv

# Resources is in same folder as main.py, so we don't need to go anywhere to get it("..")
# budget_data is our csvpath

csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csvpath, newline = "") as csvfile:

# CSV reader speficies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

# Each row is read as a row
    for row in csvreader:
        print(row) 

        