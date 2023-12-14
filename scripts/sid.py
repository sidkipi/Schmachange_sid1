import os

valid = "false"

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if file_name.startswith(("v", "V")) and file_name[1:].split("__", 1)[0].isdigit():
            print(f"File '{file_name}' matches the pattern.")
            valid = "true"
        elif file_name.startswith("R__"):
            print(f"File '{file_name}' matches the pattern.")
            valid = "true"
        else:
            print(f"Skipping file '{file_name}' based on the restricted version format.")

print(f"::set-output name=valid::{valid}")
