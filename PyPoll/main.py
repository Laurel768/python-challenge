import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
count_votes = []




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

# count the total number of voters
    for row in csvreader:
        total_votes +=1

        candidate = row[2]
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            count_votes[candidate_index] = count_votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            count_votes.append(1)

                  





print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("-------------------------")
print("Winner: ")
print("-------------------------")

f = open("analysis.txt", "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")
f.write("-------------------------\n")
f.write("-------------------------\n")
f.close()