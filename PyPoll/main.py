# Importing the os and csv module to create file paths across operating systems
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#define the variables
total_votes = 0
candidates = []
count_votes = []
percentages = []
max_index = 0
winner = ""

# open the csvfile and data is separated by commas
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

# count the total number of voters
    for row in csvreader:
        total_votes +=1

     # counting the votes for each candidate    
        candidate = row[2]
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            count_votes[candidate_index] = count_votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            count_votes.append(1)
    # calculating percentages of the votes
    max_votes = count_votes[0]
    for count in range(len(candidates)):
        vote_percentage = round(count_votes[count]/(total_votes)*100,3)
        percentages.append(vote_percentage)
        if count_votes[count] > max_votes:
            max_votes = count_votes[count]
            print(max_votes)
            max_index = count
    
    #determining the winner
    winner = candidates[max_index]

#to print on screen
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({count_votes[count]})")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

#to print to file
f = open("analysis.txt", "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")
for count in range(len(candidates)):
    f.write(f"{candidates[count]}: {percentages[count]}% ({count_votes[count]})\n")
f.write("-------------------------\n")
f.write("Winner:" + str(winner) + "\n")
f.write("-------------------------\n")
f.close()