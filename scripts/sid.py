import os
import re
import subprocess
import snowflake.connector
directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"
for entry in os.scandir(directory):
    if entry.is_file():
        file_name = entry.name
        print(file_name)
        if re.match(pattern, file_name):
            print(f"File '{file_name}' matches the pattern. Proceeding with schemachange.")
            print("Running schemachange")
            os.system('schemachange -f $GITHUB_WORKSPACE/dbscripts -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table')
        else:
            print(f"File '{file_name}' does not match the pattern. Skipping schemachange.")
            continue
