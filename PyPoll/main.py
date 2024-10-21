# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_load = "/Users/karla/Python-challenge/PyPoll/Resources/election_data.csv"
#file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
file_to_output = "/Users/karla/Python-challenge/PyPoll/analysis/election_analysis.txt"

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define a dictionary to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]  # Assuming the candidate's name is in the third column

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output = f"Election Results\n"
    output += f"-------------------------\n"
    output += f"Total Votes: {total_votes}\n"
    output += f"-------------------------\n"
    print(output)  # Print to terminal
    txt_file.write(output)  # Write to the text file

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_output)  # Print to terminal
        txt_file.write(candidate_output)  # Write to the text file

    # Generate and print the winning candidate summary
    winning_summary = f"-------------------------\n"
    winning_summary += f"Winner: {winning_candidate}\n"
    winning_summary += f"Winning Vote Count: {winning_count}\n"
    winning_summary += f"Winning Percentage: {(winning_count / total_votes) * 100:.3f}%\n"

    # Print winning candidate summary
    print(winning_summary)  # Print to terminal
    txt_file.write(winning_summary)  # Save the winning candidate summary to the text file

