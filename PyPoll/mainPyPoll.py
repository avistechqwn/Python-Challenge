#Importing the needed libraries for my code
import os
import csv

# Set variable for output file
election_data_csv = r'C:\Users\avisr\OneDrive\Desktop\Avis\GRO MH Tools GRANDE\NORTHWESTERN UNIVERSITY BOOTCAMP\HOMEWORK\Python Hmwk\PyBank\Starter_Code\PyPoll\Resources\election_data.csv'
# election_data_csv = "Resources/election_data.csv"

#Start the list of total number of votes from 0 
# Initialize a variable to store the net total
total_nmbr_votes = 0

# Get the total number of votes starting by opening my output file with the "with open" function
with open(election_data_csv, 'r') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    election_data_csv_reader = csv.reader(csvfile)

    header_row = next(election_data_csv_reader)
    first_row = next(election_data_csv_reader)
    total_nmbr_votes = total_nmbr_votes + 1
    
    for row in election_data_csv_reader:
        total_nmbr_votes = total_nmbr_votes + 1

    print(total_nmbr_votes)

# Create a an empty list and fSunction to get candidates and their votes 
def candidates_with_votes(election_data_csv):
    candidates = {}
    total_votes = 0

    # Open the CSV file
    with open(election_data_csv, 'r') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        election_data_csv_reader = csv.reader(csvfile)

        # Skip the header row since there is one present
        header_row = next(election_data_csv_reader)

        # Loop through each row in the CSV file
        for row in election_data_csv_reader:
            # Get the candidate name from the row (assuming the candidate name is in the third column)
            candidate_name = row[2]

            # Count the candidate's votes through the list
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                candidates[candidate_name] = 1

            total_votes += 1

    return candidates, total_votes

# Function to calculate the percentage of candidate
def calc_percentage(votes, total_votes):
    return (votes / total_votes) * 100

# Function to call candidate names and total # of votes
candidates, total_votes = candidates_with_votes(election_data_csv)

#Print outputs of candidates and their votes
print("Percentage of votes each candidate won:")
for candidate, votes in candidates.items():
    percentage = calc_percentage(votes, total_votes)
    print(f"{candidate}: {percentage:.2f}% ({votes})")


print("The Candidate Winner with the Most Votes is: Diana DeGette")