import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes +=1




print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("-------------------------")
print("Winner: ")
print("-------------------------")