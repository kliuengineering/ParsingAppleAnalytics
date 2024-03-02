# This program parses apple analytics from iPad Pro
# Objectives: to retrieve the battery info since it is not given explicitly by iPad OS
# Ctrl+F to find the following variables in the .txt file after this script is run
# Battery Health Level = last_value_NominalChargeCapacity / last_value_MaximumFCC * 100

import ast
import json

# The path to your "document" file
document_file_path = 'Analytics-2024-02-24-190014.ips.ca.synced'  # Update this with your actual file name
# The path to the output .txt file
output_file_path = 'parsed_dictionaries.txt'

try:
    # Open the "document" file for reading
    with open(document_file_path, 'r') as document_file:
        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Read the entire file content at once
            file_content = document_file.read().strip()
            # Split the content by new lines to get each dictionary as a separate string
            dictionaries_str = file_content.split('\n')
            # Iterate over each dictionary string
            for dict_str in dictionaries_str:
                # Ensure the string is not empty
                if dict_str.strip():
                    # Convert the string to a dictionary using json.loads
                    dictionary = json.loads(dict_str.strip())
                    # Write the dictionary to the output file
                    output_file.write(json.dumps(dictionary, indent=4) + '\n\n')  # Add an empty line after each dictionary
    print("Dictionaries have been successfully parsed and saved to", output_file_path)
except FileNotFoundError:
    print(f"File {document_file_path} not found. Please check the file path and try again.")
except json.JSONDecodeError as e:
    print(f"Error parsing a line into a dictionary using JSON: {e}. Please check the file content for correctness.")
except Exception as e:
    print(f"An error occurred: {e}")

