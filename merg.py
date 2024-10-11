

import pandas as pd
import os

# Specify the path to the original CSV file
input_file_path = './Data/merged_telegram_data.csv'

# Read the CSV file
df = pd.read_csv(input_file_path)

# Specify the required columns
required_columns = ["Channel Title", "Channel Username", "Message", "Date", "Media Path"]

# Clean the DataFrame to keep only the required columns
cleaned_df = df[required_columns]

# Specify the path for the cleaned CSV file
output_file_path = './Data/cleaned_telegram_data.csv'

# Save the cleaned DataFrame to a new CSV file
cleaned_df.to_csv(output_file_path, index=False)

print(f"Cleaned data saved to: {output_file_path}")

import pandas as pd

# Read the cleaned CSV file
cleaned_df = pd.read_csv('./Data/cleaned_telegram_data.csv')

# Print the column names
print(cleaned_df.columns.tolist())