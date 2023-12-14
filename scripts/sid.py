import os
import re

def validate_version_format(version_string, file_name):
    # Define the expected pattern for the version string
    pattern = r"^[vV]\d+\.\d+\.\d+\s*__[a-zA-Z0-9_]+\.sql$"

    # Check if the version string matches the pattern
    return bool(re.match(pattern, version_string))

# Directory containing SQL scripts
directory = "dbscripts/"

# Loop through all files in the directory
for entry in os.scandir(directory):
    if entry.is_file():
        file_name = entry.name

        # Process the file
        if validate_version_format(file_name, file_name):
            print(f"Processing file '{file_name}' with version '{file_name}'")
            # Add schemachange logic here for the valid version string
        full_command = f'schemachange -f {directory} -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table'
        # Run schemachange using subprocess.run
        #result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
         else:
            print(f"Skipping file '{file_name}' due to invalid version string")
