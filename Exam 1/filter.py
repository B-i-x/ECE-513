import re, os

# Define the regex pattern to match the URLs with variations after "/print"
url_pattern = re.compile(r'https://leam\.zybooks\.com/zybook/ARIZONAECE413SalehiFall2024/chapter/\d+ /print[^\s]*')

# Define the exact text to remove
date_string_to_remove = "10/12/24, 1 :35 PM zyBooks"

keyword_to_remove = "Salehi"

# Base directory for the files
base_dir = 'textbook'

# Input and output directories
input_dir = os.path.join(base_dir, 'raw')
output_dir = os.path.join(base_dir, 'filtered')

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each file in the input directory
for file_name in os.listdir(input_dir):
    input_file = os.path.join(input_dir, file_name)
    output_file = os.path.join(output_dir, file_name.replace('.txt', '-clean.txt'))

    # Open the input file and output file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line matches the URL pattern, contains the date string, or contains the keyword 'Salehi'
            if not url_pattern.search(line) and date_string_to_remove not in line and keyword_to_remove not in line:
                outfile.write(line)

print(f"All files have been processed and filtered content is saved in {output_dir}")