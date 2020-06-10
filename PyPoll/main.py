import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

totvotes = 0
candidates = []
candidate_votes = []
candidate_votepercent = []
candidate_tot = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader= next(csvreader)

    #print(f"Header: {csvheader}")

    for row in csvreader:

        totvotes += 1


        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes.append(1)
        else:
            candidate_votes[candidates.index(row[2])] += 1
    
    # print(f"{str(totvotes)}")
    # print(candidates)
    # print(candidate_votes)

    for i in range(len(candidates)):
        percentage = '{0:.3f}'.format(candidate_votes[i]/totvotes*100)
        candidate_votepercent.append(percentage)

    winner = max(candidate_votes)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(totvotes)}")
    print("-------------------------")
    for x in range(len(candidates)):
        print(f"{candidates[x]}: {str(candidate_votepercent[x])}% ({str(candidate_votes[x])})")
    print("-------------------------")
    print(f"Winner: {str(candidates[candidate_votes.index(winner)])}")
    print("-------------------------")

txtpath = os.path.join("analysis", "result.txt")
with open(txtpath, "w") as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {str(totvotes)}\n")
    txtfile.write("-------------------------\n")
    for x in range(len(candidates)):
        txtfile.write(f"{candidates[x]}: {str(candidate_votepercent[x])}% ({str(candidate_votes[x])})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {str(candidates[candidate_votes.index(winner)])}\n")
    txtfile.write("-------------------------\n")
