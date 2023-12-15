import os
import re


valid = "false"
pattern1 = re.compile(r'^R__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')
pattern2 = re.compile(r'^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$')
pattern3 = re.compile(r'^A__[a-zA-Z]+(?:_[a-zA-Z0-9]+)+\.(sql|SQL)$')

matching_files = []

for file_name in os.listdir("dbscripts"):
    if file_name.endswith(".sql"):
        if pattern1.match(file_name) or pattern2.match(file_name) or pattern3.match(file_name):
            print(f"File '{file_name}' matches the pattern.")
            matching_files.append(file_name)
            valid = "true"

# Set the output only if at least one file matches the pattern
if valid == "true":
    print(f"::set-output name=valid::{valid}")
    # Optionally, you can print the matching files for reference
    print("Matching files:", matching_files)

    # Trigger the workflow dispatch event
    workflow_dispatch_url = 'https://api.github.com/repos/siddevkipi/Schmachange_sid1/actions/workflows/main.yaml/dispatches'
    headers = {
        'Authorization': 'Bearer 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',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'ref': 'main'
    }
    response = requests.post(workflow_dispatch_url, headers=headers, json=payload)
    if response.status_code == 204:
        print("Workflow dispatch event triggered successfully.")
    else:
        print(f"Failed to trigger workflow dispatch event. Status code: {response.status_code}")
else:
    print("No matching files found. Exiting with success.")
    sys.exit(0)
