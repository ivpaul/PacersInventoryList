import pandas as pd
import argparse

def process_products(barcodes_file, products_file, output_base_name):
    # Read the CSV files containing barcode values and products
    barcodes_df = pd.read_csv(barcodes_file)
    products_df = pd.read_csv(products_file)

    # Count the occurrences of each unique barcode
    product_counts = products_df['Barcode'].value_counts().reset_index()

    # Rename the columns
    product_counts.columns = ['Barcode', 'Quantity']

    # Merge the DataFrames on the 'Barcode' column
    merged_df = pd.merge(barcodes_df, product_counts, on='Barcode', how='left')

    # Drop rows with NaN values in the 'Quantity' column
    merged_df.dropna(subset=['Quantity'], inplace=True)

    # Convert the 'Quantity' column to integers
    merged_df['Quantity'] = merged_df['Quantity'].astype(int)

    # Define the paths to save the new CSV and Excel files in the root of your project directory
    csv_output_file_path = f"{output_base_name}.csv"
    excel_output_file_path = f"{output_base_name}.xlsx"

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(csv_output_file_path, index=False)

    # Save the merged DataFrame to an Excel file
    merged_df.to_excel(excel_output_file_path, index=False)

    print(f"New CSV file '{csv_output_file_path}' has been created.")
    print(f"New Excel file '{excel_output_file_path}' has been created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process products and barcodes from CSV files.')
    parser.add_argument('barcodes_file', help='Input barcodes CSV file path')
    parser.add_argument('products_file', help='Input products CSV file path')
    parser.add_argument('output_base_name', help='Base name for output files (without extension)')
    args = parser.parse_args()

    process_products(args.barcodes_file, args.products_file, args.output_base_name)