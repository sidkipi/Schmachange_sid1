import os
import re
import sys

valid = "true"  # Assume all files are valid initially
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name) or pattern3.match(file_name):
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)

# Set the output only if there are matching files
if matching_files:
    print(f"::set-output name=valid::{valid}")
    # Optionally, you can print the matching files for reference
    print("Matching files:", matching_files)
else:
    print("No matching files found. Exiting with success.")
    sys.exit(0)  # Exiting the script with success status

# Continue with the workflow for all matching files
# You can add your workflow logic here
print("Workflow logic for matching files:", matching_files)
