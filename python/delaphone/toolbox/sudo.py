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

def sudo(sudo_password, cmd, user=None):
    opt = "-u {}".format(user) if user else ''
    child = pexpect.spawn("sudo {} {}".format(user, cmd))
    child.expect("[sudo]*: ")
    child.sendline(sudo_password)
    i = child.expect(['[sudo]*:', pexpect.EOF])
    if i == 0:
        raise CannotSudo()
    else:
        child.close()
        return child.exitstatus

def interactive_sudo(sudo_passwd):
    """ NOTE: client code is expected to send exit to the process. """

    child = pexpect.spawn("sudo -i")
    child.expect("[sudo]*: ")
    child.sendline(sudo_passwd)
    i = child.expect(["[sudo]*: ", "#"])
    if i == 0:
        raise CannotSudo()
    else:
        return child
