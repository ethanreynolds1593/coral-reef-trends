import os
import pandas as pd

# Define paths
input_dir = 'data/original_data'
output_dir = 'data/cleaned_data'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all CSV files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            # Read CSV file
            df = pd.read_csv(input_path, low_memory=False)

            # Basic cleaning steps
            df.columns = [col.strip() for col in df.columns]  # Strip whitespace from column names
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Strip strings
            df.drop_duplicates(inplace=True)  # Remove duplicate rows

            # Save cleaned CSV
            df.to_csv(output_path, index=False)
            print(f"Cleaned and saved: {output_path}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")
