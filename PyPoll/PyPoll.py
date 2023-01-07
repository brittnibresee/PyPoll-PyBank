import os
import csv

#set path for file
csvpath = os.path.join ("Resources", "election_data.csv")
outpath = os.path.join ("analysis", "election_data.txt")

total_votes =0
charles_votes =0
diana_votes =0
raymond_votes =0
vote_percentage =0
winning_count =0
winning_percentage =0 
winning_candidate =0
diana_percentage =0

#open and read the csv
with open (csvpath) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ',')

    next(csv_reader)

    for row in csv_reader:

        total_votes +=1
        canidate_name = row[2]


        #print canidates name with final vote count to terminal
        if canidate_name == "Charles Casper Stockham":
            charles_votes +=1
        elif canidate_name == "Diana DeGette":
            diana_votes +=1
        elif canidate_name == "Raymon Anthony Doane":
            raymond_votes +=1 
        else:
            print (f"the name of the canidate {canidate_name} is unknown")

    # Calculate percentage of votes for each candidate
    charles_percentage = (charles_votes / total_votes) * 100
    diana_percentage = (diana_votes / total_votes) * 100
    raymond_percentage = (raymond_votes / total_votes) * 100

    # Determine the winner
    if diana_votes > winning_count:
        winning_count = diana_votes
        winning_percentage = diana_percentage
        winning_candidate = "Diana DeGette"
    elif charles_votes > winning_count:
        winning_count = charles_votes
        winning_percentage = charles_percentage
        winning_candidate = "Charles Casper Stockham"
    elif raymond_votes > winning_count:
        winning_count = raymond_votes
        winning_percentage = raymond_percentage
        winning_candidate = "Raymond Anthony Doane"

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes:,}")
print("-------------------------")
print(f"Charles Casper Stockham: {charles_percentage:.3f}% ({charles_votes:,})")
print(f"Diana DeGette: {diana_percentage:.3f}% ({diana_votes:,})")
print(f"Raymond Anthony Doane: {raymond_percentage:.3f}% ({raymond_votes:,})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Save the results to a text file
with open(outpath, "w") as out_file:  
    out_file.write("Election Results")
    out_file.write("\n-------------------------")
    out_file.write(f"\nTotal Votes: {total_votes:,}")
    out_file.write("\n-------------------------")
    out_file.write(f"\nCharles Casper Stockham: {charles_percentage:.3f}% ({charles_votes:,})")
    out_file.write(f"\nDiana DeGette: {diana_percentage:.3f}% ({diana_votes:,})")
    out_file.write(f"\nRaymond Anthony Doane: {raymond_percentage:.3f}% ({raymond_votes:,})")
    out_file.write("\n-------------------------")
    out_file.write(f"\nWinner: {winning_candidate}")
    out_file.write("\n-------------------------")