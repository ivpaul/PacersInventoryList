import pandas as pd
import os

# Step 1: Read the Excel file
df = pd.read_excel('Reports.xlsx')

# Step 2: Filter rows where 'Notes' column has the value "Barcode(UPC/EAN)"
barcodes_df = df[df['Notes'] == "Barcode(UPC/EAN)"]

# Step 3: Select only the 'Product lookup' and 'Product ID' columns
barcodes_df = barcodes_df[['Product lookup', 'Product ID']]

# Step 4: Rename the columns
barcodes_df.rename(columns={'Product lookup': 'Barcode', 'Product ID': 'SKU'}, inplace=True)

# Step 5: Define the path to save the CSV file in the root of your project directory
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of the project
output_file_path = os.path.join(project_root, 'barcodes.csv')

# Step 6: Save the filtered and renamed DataFrame to a CSV file
barcodes_df.to_csv(output_file_path, index=False)

print(f"New CSV file 'barcodes_filtered.csv' has been created at {output_file_path}.")