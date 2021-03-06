#! /usr/bin/env python3

import sys
import os

import colorama
from colorama import Fore, Style

# TODO: add proper path
sys.path.append(".")
from delaphone.toolbox.user import *
from delaphone.toolbox.util import *
from delaphone.toolbox.sms import *
from delaphone.toolbox import ssh

if os.geteuid() == 0:
    print("This program should not be run as root")
    sys.exit(1)

if len(sys.argv[1:]) < 1:
    print("usage: dlp-user command")
    sys.exit(1)
command = sys.argv[1]

#elif not can_sudo():
#    print("You do not have sudo rights on this system")
#    sys.exit(1)

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
sudo_password = inputpw("Enter your password")
if not check_sudo_password(sudo_password):
    print("{}Authencation failed.{}".format(Fore.RED, Fore.RESET))
    sys.exit(1)

if command == 'add':
    print(userdetails_intro)
    username = inputs("Enter username")
    phone = inputs("Enter phone number")
    email = inputs("Enter email")
    password = generate_password()
elif command == 'delete':
    username = inputs("Enter the user to delete")

for host in ('127.0.0.1', '192.168.0.184'):
    connection = ssh.Connection(host=host, password=sudo_password)
    user = User(connection)
    if command == 'add':
        user.add(username, password)
        user.generate_ssh_keys(username)
    elif command == 'delete':
        user.delete(username)

if command == 'add':
    routesms_send(phone, "Your Linux password: {}".format(password))
