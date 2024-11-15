# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
totalMonths = 0    # initialize the total months to 0
totalNet = 0       # intitialize the total revenue to 0

# Add more variables to track other necessary financial data
monthlyChanges = []  # intialize the list of monthly net changes
months = []          # intialize the list of months
totalRevenue = 0
greatestIncrease = ["",0]
greatestDecrease = ["",1000000000]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # move to the first row
    firstRow = next(reader)

    # Extract first row to avoid appending to net_change_list

    # Track the total and net change
        # revenue is in index 1
    totalRevenue += float(firstRow[1])
    totalMonths += 1
    totalNet += float(firstRow[1])
    previousRevenue = float(firstRow[1])

    # Process each row of data
    for row in reader:
        # increment the count of the total months
        totalMonths += 1 # same as totalMonths = totalMonths + 1

        # Track the total
            # revenue is in index 1
        totalRevenue += float(row[1])

        # Track the net change
        netChange = float(row[1]) - previousRevenue
        previousRevenue = float(row[1])
        # add on to the list of monthly changes
        monthlyChanges += [netChange]
        months += [row[0]]

        # Calculate the greatest increase in profits (month and amount)
        if netChange > greatestIncrease[1]:
            greatestIncrease = [row[0], netChange] # holds the month and the value of the greatest increase

        # Calculate the greatest decrease in losses (month and amount)
        if netChange < greatestDecrease[1]:
            greatestDecrease = [row[0], netChange] # holds the month and the value of the greatest decrease

# Calculate the average net change across the months
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

# Generate the output summary
output = (
    f"\nRevenue Data Analysis \n"
    f"---------------------------\n"
    f"\tTotal Months = {totalMonths} \n"
    f"\tTotal Revenue = ${totalRevenue:,.2f} \n"
    f"\tAverage Change Per Month = ${averageChangePerMonth:,.2f} \n"
    f"\tGreatest Increase = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
    f"\tGreatest Decrease = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
    )

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
