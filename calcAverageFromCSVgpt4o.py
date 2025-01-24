import csv
from collections import defaultdict

# File input and output
input_file = "R2024_1.csv"  # Updated input file name
output_file = "averages.csv"

# Dictionary to store data; key will be a combination of employee and position
user_data = defaultdict(list)

# Read input file
with open(input_file, mode="r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract relevant fields
        user = row["Співробітник"]
        position = row["Посада"]
        # Use the correct column name "R" for calculating values
        weight = row["R"].replace(",", ".")  # Replace commas with dots, handle backticks

        try:
            # Add user's data for averaging
            user_data[(user, position)].append(float(weight))
        except ValueError:
            # Skip invalid or incorrectly formatted numbers
            continue

# Compute averages
averages = []
for (user, position), scores in user_data.items():
    avg_score = sum(scores) / len(scores) if scores else 0
    # Format data for output
    averages.append({
        "Співробітник": user,
        "Посада": position,
        "Середнє значення": f'{round(avg_score, 9)}'  # Up to 9 decimal places for precision
    })

# Write output file
with open(output_file, mode="w", encoding="utf-8", newline="") as csvfile:
    # Defining correct field order
    fieldnames = ["Співробітник", "Посада", "Середнє значення"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header and rows
    writer.writeheader()
    writer.writerows(averages)

print(f"Averages calculated and written to {output_file}")
