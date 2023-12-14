import re

def validate_version_format(version_string, file_name):
    # Define the expected pattern for the version string
    pattern = r"^V\d+\.\d+\.\d+$"

    # Check if the version string matches the pattern
    if re.match(pattern, version_string):
        return True
    else:
        print(f"Invalid version string in file '{file_name}': {version_string}. Version format must be V1.1.1")
        return False

# Examples of version strings with corresponding file names
versions_to_check = {"V1.1": "script1.sql", "V1_1": "script2.sql", "V1.2.3": "script3.sql", "V1_2_3": "script4.sql", "V1.2_3": "script5.sql"}

# Process each version string
for version, file_name in versions_to_check.items():
    if validate_version_format(version, file_name):
        print(f"Processing file '{file_name}' with version '{version}'")
        # Add schemachange logic here for the valid version string
    else:
        print(f"Skipping file '{file_name}' due to invalid version string")

# Continue with the remaining files...
