import os
import re

def validate_file_name(file_name):
    pattern1 = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"
    pattern2 = r"^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$"

    if re.match(pattern1, file_name) or re.match(pattern2, file_name):
        print(f"File '{file_name}' matches the pattern.")
        return True
    else:
        print(f"Skipping file '{file_name}' based on the restricted version format.")
        return False

def main():
    directory = "dbscripts/"
    include_files = []
    exclude_files = []

    for entry in os.scandir(directory):
        if entry.is_file():
            file_name = entry.name
            if validate_file_name(file_name):
                include_files.append(file_name)
            else:
                exclude_files.append(file_name)

    with open("include_files.txt", "w") as include_file:
        include_file.write("\n".join(include_files))

    with open("exclude_files.txt", "w") as exclude_file:
        exclude_file.write("\n".join(exclude_files))

if __name__ == "__main__":
    main()
