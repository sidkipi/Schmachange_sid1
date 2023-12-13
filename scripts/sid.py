import os
import re
import subprocess

directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"

# Get a sorted list of files in the directory
files = sorted(os.listdir(directory))

for file_name in files:
    full_path = os.path.join(directory, file_name)

    if os.path.isfile(full_path) and re.match(pattern, file_name):
        print(f"File '{file_name}' matches the allowed pattern. Proceeding with schemachange.")
        print("Running schemachange")

        # Build the full schemachange command
        full_command = f'schemachange -f {directory} -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -i {file_name}'

        # Run schemachange using subprocess.run
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print("schemachange executed successfully.")
        else:
            print(f"Error executing schemachange. Exit code: {result.returncode}")
            print("Output:", result.stdout)
            print("Errors:", result.stderr)
