import os
import re
import subprocess

directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"

# Use os.scandir to get a list of files in the directory
for entry in os.scandir(directory):
    if entry.is_file():
        # Extract the file name from the full path
        file_name = entry.name
        print(file_name)

        # Check if the file name matches the pattern
        if re.match(pattern, file_name):
            print(f"File '{file_name}' matches the pattern. Proceeding with schemachange.")

            # Add schemachange logic here
            schemachange_command = (
                f"schemachange -f {directory} -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE "
                f"-w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table"
            )
            subprocess.run(schemachange_command, shell=True, check=True)
            
        else:
            print(f"File '{file_name}' does not match the pattern. Skipping schemachange.")
            # Skip schemachange for files that do not match the pattern
            continue
