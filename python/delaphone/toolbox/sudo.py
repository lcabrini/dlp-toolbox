import shlex
import subprocess
import pexpect

class CannotSudo(Exception):
    pass

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

def sudo(sudo_password, cmd):
    child = pexpect.spawn("sudo {}".format(cmd))
    child.expect("[sudo]*: ")
    child.sendline(sudo_password)
    i = child.expect(['[sudo]*:', '*'])
    if i == 0:
        raise CannotSudo()
    else:
        return child
