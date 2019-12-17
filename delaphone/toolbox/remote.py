import os
import time
import re
from getpass import getuser
import paramiko
from delaphone.toolbox.host import Host

class RemoteHost(Host):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, username=self.username,
                password=self.password)

    def run(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        out = [o.strip() for o in stdout.readlines()]
        err = [e.strip() for e in stderr.readlines()]
        ret = stdout.channel.recv_exit_status()
        return ret, out, err

    def sudo(self, cmd, **kwargs):
        if 'user' in kwargs:
            cmd = "sudo -Su {} {}".format(kwargs['user'], cmd)
        else:
            cmd = "sudo -S {}".format(cmd)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        time.sleep(0.1)
        stdin.write("{}\n".format(self.password))
        out = [o.strip() for o in stdout.readlines()]
        err = [e.strip() for e in stderr.readlines()]
        if len(err) > 0:
            err[0] = re.sub(r'\[sudo\].+?: ', '', err[0])
        ret = stdout.channel.recv_exit_status()
        return ret, out, err

    def __str__(self):
        return self.host
