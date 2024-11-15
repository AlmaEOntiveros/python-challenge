# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidateNames = []
candidateVotes = {}

# Winning Candidate and Winning Count Tracker
winningCandidate = ""
winningCount = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidateName = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidateName not in candidateNames:
            # if the candidate is not in the list, add the flavor candidate to the list of candidates
            candidateNames.append(candidateName)

            # add the value to the dictionary as well
            # { "key": value}
            # start the count at 1 for the votes
            candidateVotes[candidateName] = 0

        
            # the candidate is in the list of candidate's
        # Add a vote to the candidate's count
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1
print(candidateNames)
print(candidateVotes)
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidateVotes:
    # Get the vote count and calculate the percentage
        votes = candidateVotes.get(candidate)
        votePct = (float(votes) / float(total_votes)) * 100.00
        if votes > winningCount:
            # update the votes to be the new winning count
            winningCount = votes
            # update the winning candidate
            winningCandidate= candidate

           
        voteOutput = f"\t{candidate}: {votePct:.2f}% \n"

            # Update the winning candidate if this one has more votes


            # Print and save each candidate's vote count and percentage
        print(voteOutput)
        txt_file.write(voteOutput)
    # Generate and print the winning candidate summary
     # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winningCandidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #print(output)

# Save the winning candidate summary to the text file
#with open(outputFile, "w") as textFile:
    txt_file.write(winning_candidate_summary)
