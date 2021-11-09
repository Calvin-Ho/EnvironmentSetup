#!/usr/bin/env/python

'''
Helper script to remove the Apple quarantine attribute from a specified filesystem entity
'''

import os
import sys
import subprocess

ATTRIBUTES_COMMAND = "xattr "
APPLE_LOCK_ATTRIBUTE = "com.apple.quarantine "
UNLOCK_COMMAND = f"{ATTRIBUTES_COMMAND} -d {APPLE_LOCK_ATTRIBUTE}"

def unlock_file(entity_name: str) -> bool:
    '''
    Reads the filesystem entity's extended attributes, checking for the 'com.apple.quarantine'
    locking attribute, and attempts to unlock it if it exists.
    '''
    # Read file's extended attributes to determine if APPLE_LOCK_ATTRIBUTE is present
    attributes = subprocess.check_output(f"{ATTRIBUTES_COMMAND} '{entity_name}'", shell=True)

    # Decode returned byte strings from stdout based on system encoding
    attributes = attributes.decode(sys.stdout.encoding)

    # Unlock file if attribute is present, printing message if the atribute is not found
    if APPLE_LOCK_ATTRIBUTE.rstrip() in attributes:
        return os.system(f"{UNLOCK_COMMAND} '{entity_name}'") == 0
    else:
        print(f"Lock attribute not found for {entity_name}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: xattr-unlock <path> ...")
        sys.exit(os.EX_USAGE)

    locked_files = sys.argv[1:]
    unlocked_files = 0

    for f_name in locked_files:
        if unlock_file(f_name):
            unlocked_files += 1

    print(f"\n\t{unlocked_files} files unlocked of {len(locked_files)} given")

if __name__ == "__main__":
    main()
