import os
import time
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
        return stdout.readlines()

    def sudo(self, cmd, **kwargs):
        if 'user' in kwargs:
            cmd = "sudo -u {} {}".format(kwargs['user'], cmd)
        else:
            cmd = "sudo {}".format(cmd)
        stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty=True)
        time.sleep(0.1)
        stdin.write("{}\n".format(self.password))
        return stdout.readlines()[2:]
