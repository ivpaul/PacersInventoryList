A python script to drastically reduce the time spent performing inventory scans at the running store I work at.

Inventory scans are more time efficient when the bproduct arcodes are inputted into a Google/Excel Sheet, downloaded as a CSV file, then uploaded to this script.  The output of this script produces both a XLSX and CSV file of the final inventory count.

Takes in the following CLI arguments: python main.py barcodes.csv {products_file.csv} {output_title}
