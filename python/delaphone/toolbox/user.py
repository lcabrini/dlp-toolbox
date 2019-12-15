import string
import random
import subprocess
import shlex
import pexpect
from delaphone.toolbox.sudo import *

class UserExists(Exception):
    pass

def generate_password():
    # This may change later.
    pw = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
    pw += "-"
    pw += ''.join(random.choice(string.digits) for i in range(6))
    return pw

def user_exists(username):
    with open("/etc/passwd", "r") as file:
        for line in file:
            if line.startswith("{}:".format(username)):
                return True
    return False

def add_user(sudo_password, username, password):
    if user_exists(username):
        raise UserExists()

    child = interactive_sudo(sudo_password)
    child.sendline("useradd -m {}".format(username))
    child.expect("#")
    child.sendline("chpasswd <<< '{}:{}'".format(username, password))
    child.expect("#")
    child.close()
