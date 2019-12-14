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
