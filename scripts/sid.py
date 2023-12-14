import os
import re

valid = "false"
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name):
            print(f"File '{file_name}' matches the pattern.")
            valid = "true"
        else:
            print(f"Skipping file '{file_name}' based on the restricted version format.")

print(f"::set-output name=valid::{valid}")
