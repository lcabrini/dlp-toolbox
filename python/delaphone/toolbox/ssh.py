import time
import paramiko

class Connection():
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, username=username, password=password)

    def run(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.readlines()

    def sudo(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(
                "sudo {}".format(cmd), get_pty=True)
        time.sleep(0.1)
        stdin.write("{}\n".format(self.password))
        return stdout.readlines()[2:]
