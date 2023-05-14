import csv
import os

# Get the path to the CSV file and result file
dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, 'Resource', 'budget_data.csv')
analysis_result_path = os.path.join(dir_path, 'Resource', 'budget_data_analysis.txt')

def analyze_budget_data(csv_file):
    # Set up variables
    total_months = 0
    net_profit_loss = 0
    previous_profit_loss = 0
    profit_loss_change_list = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    # Open the CSV file
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the header row
        next(csvreader)

        # Loop through the rows in the CSV file
        for row in csvreader:

            # Increment the total number of months
            total_months += 1

            # Add the profit/loss for this row to the net total
            net_profit_loss += int(row[1])

            # Calculate the profit/loss change from the previous month
            if total_months > 1:
                profit_loss_change = int(row[1]) - previous_profit_loss
                profit_loss_change_list.append(profit_loss_change)

                # Check if this change is the greatest increase or decrease
                if profit_loss_change > greatest_increase[1]:
                    greatest_increase = [row[0], profit_loss_change]
                elif profit_loss_change < greatest_decrease[1]:
                    greatest_decrease = [row[0], profit_loss_change]

            # Save this month's profit/loss for use in the next iteration
            previous_profit_loss = int(row[1])

    # Calculate the average change
    average_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

    # Create a string with the analysis results in the requested format
    analysis_results = f"Financial Analysis\n\n----------------------------\n\nTotal Months: {total_months}\nTotal: ${net_profit_loss}\nAverage Change: ${average_change:.2f}\nGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\nGreatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"

    # Print the analysis results to the terminal
    print(analysis_results)

    # Export the analysis results to a text file in the Resource folder
    with open(analysis_result_path, 'w') as file:
        file.write(analysis_results)


# Analyze the budget data and export the results to a text file
analyze_budget_data(csv_path)
