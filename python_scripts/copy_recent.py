#!/usr/bin/env/python

'''
Helper script to copy a recent notes file that is named with a date in the format
MM-DD-YY.  If a file by that name already exists, abort and do nothing.
'''

import os
import sys
import subprocess
import re
from datetime import date

GET_LATEST_FILE_COMMAND = "ls -t -1 | head -1"

def main():
    # Find the most recent file in the current directory
    latest_file = subprocess.check_output(GET_LATEST_FILE_COMMAND, shell=True)
    latest_file = latest_file.decode(sys.stdout.encoding)

    current_date = date.today().strftime("%-m-%-d-%y")

    # Remove the date portion from recent file's name and replace with today's date
    new_filename = re.sub(r"(\d{1,2}-\d{1,2}-\d{1,2})", current_date, latest_file)

    latest_file, new_filename = latest_file.strip(), new_filename.strip()

    # Save the name of this script for printing messages
    script_name = os.path.basename(__file__)

    # Check to see if we already have a file by this new name to prevent overwriting
    if not os.path.exists(new_filename):
        # Copy the old as a newly renamed file
        os.system(f"cp {latest_file} {new_filename}")
        print(f"{script_name}: Copied new file with name {new_filename}")
    else:
        sys.exit(f"{script_name}: File with today's date already exists, aborting.")

if __name__ == "__main__":
    main()
