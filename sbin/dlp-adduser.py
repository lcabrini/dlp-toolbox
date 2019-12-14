#! /usr/bin/env python3

import sys
import os

import colorama
from colorama import Fore, Style

# TODO: add proper path
sys.path.append("python")
from delaphone.toolbox.util import *

if os.geteuid() == 0:
    print("This program should not be run as root")
    sys.exit(1)

colorama.init()

sudo_intro = """
You will be required to give your password for sudo access. This will
be used both on the local and remote hosts.

{}It is therefore assumed that your password is the same on all the
affected hosts and that you have sudo rights on all the hosts.{}

If this is not the case you may want to exit now.
""".format(Fore.YELLOW, Style.RESET_ALL)

userdetails_intro = """
You will need to enter the details of the new user. The phone number is
important because it will be used to send an SMS with the user's initial
password. The email address will be used to send a welcome message.
"""

print(sudo_intro.strip())
if not ask_yesno("Do you want to continue"):
    sys.exit(1)
password = inputpw("Enter your password")

print(userdetails_intro)
username = input("Enter username: ")
password = input("Enter phone number: ")
email = input("Enter email: ")