import os
import csv

# Get the path to the CSV file and result file
dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, 'Resource', 'election_data.csv')

def analyze_election_data(data_file):
    # Initialize variables
    total_votes = 0
    candidates = {}
    winner_votes = 0
    winner = ""

    # Read the CSV file
    with open(data_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the header row
        next(csvreader)

        # Loop through the rows
        for row in csvreader:
            # Increment the vote count
            total_votes += 1

            # Get the candidate name from the row
            candidate = row[2]

            # Add the candidate to the dictionary of candidates if not already present
            if candidate not in candidates:
                candidates[candidate] = 0

            # Increment the vote count for the candidate
            candidates[candidate] += 1

    # Build the result string
    result = "Election Results\n\n"
    result += "-------------------------\n\n"
    result += f"Total Votes: {total_votes}\n\n"
    result += "-------------------------\n"
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        result += f"{candidate}: {percentage:.3f}% ({votes})\n"
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate
    result += "-------------------------\n\n"
    result += f"Winner: {winner}\n\n"
    result += "-------------------------\n"

     # Print the analysis result to the terminal
    print(result)

    # Write the result string to a text file
    output_file = os.path.splitext(data_file)[0] + "_results.txt"
    with open(output_file, "w") as file:
        file.write(result)

# Analyze the election data and export the results to a text file
analyze_election_data(csv_path)