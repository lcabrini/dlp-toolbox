import string
import random
from delaphone.toolbox.tool import Tool

class UserExists(Exception): pass
class KeyPairExists(Exception): pass

class User(Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def exists(self, username):
        cmd = "grep '^{}:' /etc/passwd".format(username)
        return len(self.handler.run(cmd)) > 0

    def add(self, username, password):
        if self.exists(username):
            raise UserExists("user {} already exists on {}".format(
                username, self.handler.host))

        self.handler.sudo("useradd -m {}".format(username))
        self.handler.sudo("chpasswd <<< '{}:{}'".format(username, password))

    def delete(self, username):
        self.handler.sudo("userdel -r {}".format(username))

    def generate_ssh_keys(self, username):
        keyfile = '/home/{}/.ssh/id_rsa'.format(username)
        cmd = "test -f {} && echo true".format(keyfile)
        ans = self.handler.sudo(cmd, user=username)
        has_keyfile = len(ans) > 0

        if has_keyfile:
            msg = "user {} already has a default SSH key on {}".format(
                    username, self.handler.host)
            raise KeyPairExists(msg)

        cmd = "ssh-keygen -q -t rsa -N '' -f {}".format(keyfile)
        self.handler.sudo(cmd, user=username)
