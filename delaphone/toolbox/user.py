import string
import random
from delaphone.toolbox.tool import Tool

class UserExists(Exception): pass
class KeyPairExists(Exception): pass

# TODO: rename all 'self.conn' to 'self.handler'

class User(Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def exists(self, username):
        cmd = "grep '^{}:' /etc/passwd".format(username)
        return len(self.conn.run(cmd)) > 0

    def add(self, username, password):
        if self.exists(username):
            raise UserExists("user {} already exists on {}".format(
                username, self.conn.host))

        self.conn.sudo("useradd -m {}".format(username))
        self.conn.sudo("chpasswd <<< '{}:{}'".format(username, password))

    def delete(self, username):
        self.conn.sudo("userdel -r {}".format(username))

    def generate_ssh_keys(self, username):
        keyfile = '/home/{}/.ssh/id_rsa'.format(username)
        cmd = "test -f {} && echo true".format(keyfile)
        ans = self.conn.sudo(cmd, user=username)
        has_keyfile = len(ans) > 0

        if has_keyfile:
            msg = "user {} already has a default SSH key on {}".format(
                    username, self.conn.host)
            raise KeyPairExists(msg)

        cmd = "ssh-keygen -q -t rsa -N '' -f {}".format(keyfile)
        self.conn.sudo(cmd, user=username)
