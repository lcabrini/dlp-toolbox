import subprocess
import shlex

def can_sudo():
    cmd = shlex.split("sudo -nv")
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        return e.output.decode().startswith("sudo:")
