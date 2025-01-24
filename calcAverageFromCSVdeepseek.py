import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('R 2024.xlsx - Усі по місяцям.csv', delimiter=',')

# Replace commas with dots in the 'Результат' column and convert to numeric
df['Результат'] = df['Результат'].astype(str).str.replace(',', '.').astype(float)

# Group by 'Співробітник' and calculate the average for each user
average_results = df.groupby('Співробітник')['Результат'].mean().reset_index()

# Rename the columns for clarity
average_results.columns = ['Співробітник', 'Середній результат']

# Save the results to a new CSV file
average_results.to_csv('average_deepseek.csv', index=False, encoding='utf-8-sig')

print("Average results have been saved to 'average_deepseek.csv'")