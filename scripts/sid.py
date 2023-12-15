import os
import re
import shutil
import sys

valid = "false"
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []
unmatched_files = []

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name) or pattern3.match(file_name):
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)
            valid = "true"
        else:
            print(f"File '{file_name}' does not match the pattern. Adding to unmatched files.")
            unmatched_files.append(file_name)

# Set the output only if at least one file matches the pattern
if valid == "true":
    print(f"::set-output name=valid::{valid}")
    # Optionally, you can print the matching files for reference
    print("Matching files:", matching_files)

    # Copy unmatched files to a separate directory
    unmatched_dir = "dbscripts/unmatched"
    os.makedirs(unmatched_dir, exist_ok=True)
    for file_name in unmatched_files:
        source_path = os.path.join("dbscripts", file_name)
        destination_path = os.path.join(unmatched_dir, file_name)
        shutil.copy2(source_path, destination_path)

    # Optionally, you can start the workflow here
else:
    print("No matching files found. Exiting with success.")
    if unmatched_files:
        print("Unmatched files:", unmatched_files)
        # Copy unmatched files to a separate directory
        unmatched_dir = "dbscripts/unmatched"
        os.makedirs(unmatched_dir, exist_ok=True)
        for file_name in unmatched_files:
            source_path = os.path.join("dbscripts", file_name)
            destination_path = os.path.join(unmatched_dir, file_name)
            shutil.copy2(source_path, destination_path)

    sys.exit(0)
