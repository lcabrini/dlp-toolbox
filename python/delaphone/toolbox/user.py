import string
import random
import subprocess
import shlex
import pexpect

def can_sudo():
    cmd = shlex.split("sudo -nv")
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        return e.output.decode().startswith("sudo:")

def check_sudo_password(password):
    child = pexpect.spawn("sudo echo 1")
    child.expect("[sudo]*: ")
    child.sendline(password.encode())
    i = child.expect(['[sudo]*:', '1'])
    if i == 0:
        return False
    elif i == 1:
        return True
    else:
        # Hopefully we never get here
        return False

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
