import os
import re
import sys

valid = "true"  # Assume all files are valid initially
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []
non_matching_files = []

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name) or pattern3.match(file_name):
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)
        else:
            print(f"File '{file_name}' does not match the pattern.")
            non_matching_files.append(file_name)
            valid = "false"

# Optionally, you can print the matching files for reference
print("Matching files:", matching_files)

# Set the output and exit only if all files match the pattern
if valid == "true":
    print(f"::set-output name=valid::{valid}")
else:
    print("Some files do not match the pattern. Exiting with failure.")
    print("Non-matching files:", non_matching_files)
    sys.exit(1)  # Exiting the script with failure status
