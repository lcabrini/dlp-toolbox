#! /usr/bin/python3

import sys
import os
from getpass import getpass

# TODO: add proper path
sys.path.append("python")
from delaphone.toolbox.util import ask_yesno

if os.geteuid() == 0:
    print("This program should not be run as root")
    sys.exit(1)

sudo_intro = """
You will be required to give your password for sudo access. This will
be used both on the local and remote hosts. It is therefore assumed that
your password is the same on all the affected hosts and that you have
sudo rights on all the hosts.

If this is not the case you may want to exit now.
"""

print(sudo_intro.strip())
if not ask_yesno("Do you want to continue"):
    sys.exit(1)

password = getpass("Enter your password: ")
print()
username = input("Enter username: ")
password = input("Enter phone number: ")
email = input("Enter email: ")
