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

def unlock_entity(entity_name: str) -> bool:
    # Read entity's extended attributes to determine if APPLE_LOCK_ATTRIBUTE is present
    attributes = subprocess.check_output(f"{ATTRIBUTES_COMMAND} '{entity_name}'", shell=True)

    # Decode all returned byte strings based on system encoding
    attributes = attributes.decode(sys.stdout.encoding)

    # Unlock entity if attribute is present, printing message if the attribute is not found
    if APPLE_LOCK_ATTRIBUTE.rstrip() in attributes:
        return os.system(f"{UNLOCK_COMMAND} '{entity_name}'") == 0
    else:
        print(f"Lock attribute not found for {entity_name}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: xattr-unlock <path> ...")
        sys.exit(os.EX_USAGE)

    locked_entities = sys.argv[1:]

    unlocked_entities = 0

    for name in locked_entities:
        if unlock_entity(name):
            unlocked_entities += 1

    print(f"\n\t{unlocked_entities} files unlocked of {len(locked_entities)} given")

if __name__ == "__main__":
    main()
