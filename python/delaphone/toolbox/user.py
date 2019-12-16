import string
import random

class UserExists(Exception):
    pass

class User():
    def __init__(self, connection):
        self.conn = connection

    def exists(self, username):
        cmd = "grep '^{}:' /etc/passwd".format(username)
        return len(self.conn.run(cmd)) > 0

    def add(self, username, password=None):
        if self.exists(username):
            raise UserExists("user {} already exists on {}".format(
                username, self.conn.host))

        if password is None:
            password = self.generate_password()

        self.conn.sudo("useradd -m {}".format(username))
        self.conn.sudo("chpasswd <<< '{}:{}'".format(username, password))

    def delete(self, username):
        conn.sudo("userdel -r {}".format(username))

    def generate_password(self):
        # This may change later.
        uc = string.ascii_uppercase
        pw = ''.join(random.choice(uc) for i in range(3))
        pw += "-"
        pw += ''.join(random.choice(string.digits) for i in range(6))
        return pw

    def generate_ssh_keys(username, sudo_password):
        keyfile = '/home/{}/.ssh/id_rsa'.format(username)
        cmd = "ssh-keygen -q -t rsa -N '' -f {}".format(keyfile)
        conn.sudo(cmd)
