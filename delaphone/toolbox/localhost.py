import time
import subprocess
from subprocess import Popen, PIPE
import shlex
from delaphone.toolbox.host import Host

class Localhost(Host):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, cmd):
        args = shlex.split(cmd)
        try:
            with Popen(args, stdout=PIPE, stdin=PIPE) as p:
                out, err = p.communicate()
            return p.returncode, out, err
        except FileNotFoundError:
            raise NoSuchCommand(args[0])

    def sudo(self, cmd, **kwargs):
        if not 'password' in kwargs:
            raise MissingPassword()

        if 'user' in kwargs:
            cmd = 'sudo -Su {} {}'.format(kwargs['user'], cmd)
        else:
            cmd = 'sudo -S {}'.format(cmd)

        args = shlex.split(cmd)
        with Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE) as p:
            passwd = "{}\n".format(self.password).encode()
            out, err = proc.communicate(passwd)
        return p.returncode, out, err
