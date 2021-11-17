# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Add dependencies

import csv
import os

# Assign a variable for the file to load and the path.

file_to_load="/Users/marciociano/Documents/GitHub/Election_Analysis/Resources/election_results.csv"

# Assign a variable to save the file to a path.

file_to_save = "/Users/marciociano/Documents/GitHub/Election_Analysis/analysis/election_analysis.txt"

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
     file_reader = csv.reader(election_data)

     # Print each row in the CSV file.
for row in file_reader:
        print(row)