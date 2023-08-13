import os
import csv

# Set variable for output file
#budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')
budget_data_csv = "Resources/budget_data.csv"

total_months = 0

#  Open the output file
with open(budget_data_csv, 'r') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    budget_data_csv_reader = csv.reader(csvfile)

    header_row = next(budget_data_csv_reader)
    first_row = next(budget_data_csv_reader)
    total_months = total_months + 1
    
    for row in budget_data_csv_reader:
        total_months = total_months + 1

    print(total_months)

# Initialize a variable to store the net total
net_total = 0

#  Open the output file
with open(budget_data_csv, 'r') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    budget_data_csv_reader = csv.reader(csvfile)
    
    header_row = next(budget_data_csv_reader)
    first_row = next(budget_data_csv_reader)
   
    
    for row in budget_data_csv_reader:
        try:
            net_total += int(row[1])  # Assuming the "Profit/Losses" column is at index 1
        except ValueError:
            continue

    print(net_total) #21475215
    print(f"The net total amount of 'Profit/Losses' over the entire period is: ${net_total}")


def calc_avgchange(budget_data_csv):
    # Initialize variables to store changes and the sum of changes
    changes = []
    sum_changes = 0

    # Open the CSV file
    with open("Resources/budget_data.csv", 'r') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        budget_data_csv_reader = csv.reader(csvfile)

        # Skip the header row if it exists
        header = next(budget_data_csv_reader, None)

        # Initialize a variable to store the previous "Profit/Losses" value
        prev_value = None

        # Loop through each row in the CSV file
        for row in budget_data_csv_reader:
            # Convert the "Profit/Losses" value to an integer
            current_value = int(row[1])  # Assuming the "Profit/Losses" column is at index 1

            # Calculate the change from the previous value (except for the first row)
            if prev_value is not None:
                change = current_value - prev_value
                changes.append(change)
                sum_changes += change

            # Update the previous value for the next iteration
            prev_value = current_value

    # Calculate the average of changes
    if len(changes) > 0:
        average_change = sum_changes / len(changes)
    else:
        average_change = 0


    #return changes, average_change
    return average_change
    # print(average_change)
    
# Recalling my csv file path for my average_change function
bd_csv_file_path = "Resources/budget_data.csv"  
average_change = calc_avgchange(bd_csv_file_path)

# print("Changes in 'Profit/Losses' over the entire period:", changes)
print(f"Average change in 'Profit/Losses': ${average_change}")


#Calling and defining a function for the greatest increase in profits (date and amount) over the entire period
def greatest_inc(budget_data_csv):
    # Initialize variables to store the greatest increase and its corresponding date
    max_increase = 0
    max_date = None

    # Open the CSV file
    with open("Resources/budget_data.csv", 'r') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        budget_data_csv_reader = csv.reader(csvfile)

        # Skip the header row if it exists
        header = next(budget_data_csv_reader, None)

        # Initialize a variable to store the previous "Profit/Losses" value
        prev_value = None

        # Loop through each row in the CSV file
        for row in budget_data_csv_reader:
            # Convert the "Profit/Losses" value to an integer
            current_value = int(row[1])  # Assuming the "Profit/Losses" column is at index 1

            # Calculate the change from the previous value (except for the first row)
            if prev_value is not None:
                change = current_value - prev_value

                # Check if the current change is greater than the current maximum increase
                if change > max_increase:
                    max_increase = change
                    max_date = row[0]  # Assuming the "Date" column is at index 0

            # Update the previous value for the next iteration
            prev_value = current_value

    return max_date, max_increase

# Recalling my csv file path for my max date and increase function
bd_csv_file_path = "Resources/budget_data.csv"  
max_date, max_increase = greatest_inc(bd_csv_file_path)

print(f"The greatest increase in profits occurred on {max_date} with an amount of ${max_increase}")


#The greatest increase in profits (date and amount) over the entire period
def greatest_dec(budget_data_csv):
    # Initialize variables to store the greatest increase and its corresponding date
    max_decrease = 0
    maxd_date = None

    # Open the CSV file
    with open("Resources/budget_data.csv", 'r') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        budget_data_csv_reader = csv.reader(csvfile)

        # Skip the header row if it exists
        header = next(budget_data_csv_reader, None)

        # Initialize a variable to store the previous "Profit/Losses" value
        prev_value = None

        # Loop through each row in the CSV file
        for row in budget_data_csv_reader:
            # Convert the "Profit/Losses" value to an integer
            current_value = int(row[1])  # Assuming the "Profit/Losses" column is at index 1

            # Calculate the change from the previous value (except for the first row)
            if prev_value is not None:
                change = current_value - prev_value

                # Check if the current change is greater than the current maximum increase
                if change < max_decrease:
                    max_decrease = change
                    maxd_date = row[0]  # Assuming the "Date" column is at index 0

            # Update the previous value for the next iteration
            prev_value = current_value

    return maxd_date, max_decrease

# Recalling my csv file path for my max date and decrerease function
bd_csv_file_path = "Resources/budget_data.csv"  
maxd_date, max_decrease = greatest_dec(bd_csv_file_path)

print(f"The greatest decrease in profits occurred on {maxd_date} with an amount of ${max_decrease}")


print("Final Analysis")
print(f"Total Months: ${total_months}")
print(f"The net total amount of 'Profit/Losses' over the entire period is: ${net_total}")
print(f"Average change in 'Profit/Losses': ${average_change}")
print(f"The greatest increase in profits occurred on {max_date} with an amount of ${max_increase}")
print(f"The greatest decrease in profits occurred on {maxd_date} with an amount of ${max_decrease}")




# ```text
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)