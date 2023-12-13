import os
import re
import subprocess
import snowflake.connector

directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+_[a-zA-Z0-9_]+\.sql$"

for entry in os.scandir(directory):
    if entry.is_file():
        file_name = entry.name
        print(file_name)
        
        if not re.match(pattern, file_name):
            print(f"File '{file_name}' does not match the allowed pattern. Skipping schemachange.")
            continue

        print(f"File '{file_name}' matches the allowed pattern. Proceeding with schemachange.")
        print("Running schemachange")

        # Build the full schemachange command
        full_command = f'schemachange -f {directory} -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table'

        # Run schemachange using subprocess.run
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print("schemachange executed successfully.")
        else:
            print(f"Error executing schemachange. Exit code: {result.returncode}")
            print("Output:", result.stdout)
            print("Errors:", result.stderr)
