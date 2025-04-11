import os
import pandas as pd

# Define paths
input_dir = 'data/cleaned_data'
output_dir = 'data/processed_data'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all CSV files in the cleaned data directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            # Load cleaned data
            df = pd.read_csv(input_path)

            # ===== Example Processing Steps =====
            # Convert date columns to datetime if present
            for col in df.columns:
                if 'date' in col.lower():
                    df[col] = pd.to_datetime(df[col], errors='coerce')

            # Convert numeric columns (if not already)
            for col in df.select_dtypes(include='object').columns:
                df[col] = pd.to_numeric(df[col], errors='ignore')

            # Add a simple feature: row count index (useful for plotting/time series)
            df['row_index'] = range(len(df))

            # Save processed CSV
            df.to_csv(output_path, index=False)
            print(f"Processed and saved: {output_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
