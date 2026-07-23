Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

==================================================== RESTART: C:/Users/surya/AppData/Local/Programs/Python/Python314/playtennis.csv ====================================================
Training Data:
['import csv']
[]
['# Read dataset']
['with open("playtennis.csv") as file:']
['    data = list(csv.reader(file))']
[]
['print("Training Data:")']
['for row in data:']
['    print(row)']
[]
['# Remove header']
['data = data[1:]']
[]
['# Initialize hypothesis']
['hypothesis = None']
[]
['for row in data:']
["    if row[-1].lower() in ['yes'", " 'positive']:"]
['        if hypothesis is None:']
['            hypothesis = row[:-1]']
['        else:']
['            for i in range(len(hypothesis)):']
['                if hypothesis[i] != row[i]:']
["                    hypothesis[i] = '?'"]
[]
['print("\\nFinal Hypothesis:")']
['print(hypothesis)']
Traceback (most recent call last):
  File "C:/Users/surya/AppData/Local/Programs/Python/Python314/playtennis.csv", line 18, in <module>
    if row[-1].lower() in ['yes', 'positive']:
IndexError: list index out of range

==================================================== RESTART: C:/Users/surya/AppData/Local/Programs/Python/Python314/playtennis.csv ====================================================
TRAINING DATASET

['import csv']
[]
['# Read the CSV file']
['with open("playtennis.csv"', ' "r") as file:']
['    data = list(csv.reader(file))']
[]
['# Display the dataset']
['print("TRAINING DATASET\\n")']
['for row in data:']
['    print(row)']
[]
['# Separate header and data']
['header = data[0]']
['examples = data[1:]']
[]
['hypothesis = None']
[]
['print("\\nFIND-S ALGORITHM EXECUTION\\n")']
[]
['for row in examples:']
[]
['    # Skip empty rows']
['    if len(row) == 0:']
['        continue']
[]
['    # Check only positive examples']
['    if row[-1].strip().lower() == "yes":']
[]
['        print("Positive Example:"', ' row[:-1])']
[]
['        # Initialize hypothesis with first positive example']
['        if hypothesis is None:']
['            hypothesis = row[:-1].copy()']
[]
['        else:']
['            # Compare attributes']
['            for i in range(len(hypothesis)):']
['                if hypothesis[i] != row[i]:']
['                    hypothesis[i] = "?"']
[]
['        print("Current Hypothesis:"', ' hypothesis)']
['        print()']
[]
['# Print final hypothesis']
['print("=" * 50)']
['print("FINAL HYPOTHESIS")']
['print(hypothesis)']
['print("=" * 50)']

FIND-S ALGORITHM EXECUTION

==================================================
FINAL HYPOTHESIS
None
==================================================

=============================================================================== RESTART: F:/PYTON/find.py ==============================================================================
TRAINING DATASET

['import csv']
[]
['# Read the CSV file']
['with open("playtennis.csv"', ' "r") as file:']
['    data = list(csv.reader(file))']
[]
['# Display the dataset']
['print("TRAINING DATASET\\n")']
['for row in data:']
['    print(row)']
[]
['# Separate header and data']
['header = data[0]']
['examples = data[1:]']
[]
['hypothesis = None']
[]
['print("\\nFIND-S ALGORITHM EXECUTION\\n")']
[]
['for row in examples:']
[]
['    # Skip empty rows']
['    if len(row) == 0:']
['        continue']
[]
['    # Check only positive examples']
['    if row[-1].strip().lower() == "yes":']
[]
['        print("Positive Example:"', ' row[:-1])']
[]
['        # Initialize hypothesis with first positive example']
['        if hypothesis is None:']
['            hypothesis = row[:-1].copy()']
[]
['        else:']
['            # Compare attributes']
['            for i in range(len(hypothesis)):']
['                if hypothesis[i] != row[i]:']
['                    hypothesis[i] = "?"']
[]
['        print("Current Hypothesis:"', ' hypothesis)']
['        print()']
[]
['# Print final hypothesis']
['print("=" * 50)']
['print("FINAL HYPOTHESIS")']
['print(hypothesis)']
['print("=" * 50)']

FIND-S ALGORITHM EXECUTION

==================================================
FINAL HYPOTHESIS
None
==================================================
>>> 
=============================================================================== RESTART: F:/PYTON/find.py ==============================================================================
TRAINING DATASET

['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'PlayTennis']
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No']
['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes']
['Rainy', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'No']
['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'Yes']

FIND-S ALGORITHM EXECUTION

Positive Example: ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
Current Hypothesis: ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']

Positive Example: ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same']
Current Hypothesis: ['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']

Positive Example: ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same']
Current Hypothesis: ['Sunny', 'Warm', '?', 'Strong', '?', 'Same']

Positive Example: ['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same']
Current Hypothesis: ['Sunny', 'Warm', '?', '?', '?', 'Same']

==================================================
FINAL HYPOTHESIS
['Sunny', 'Warm', '?', '?', '?', 'Same']
==================================================
