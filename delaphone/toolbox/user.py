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

    def add(self, username, password):
        if self.exists(username):
            raise UserExists("user {} already exists on {}".format(
                username, self.conn.host))

        self.conn.sudo("useradd -m {}".format(username))
        self.conn.sudo("chpasswd <<< '{}:{}'".format(username, password))

    def delete(self, username):
        self.conn.sudo("userdel -r {}".format(username))


    def generate_ssh_keys(username, sudo_password):
        keyfile = '/home/{}/.ssh/id_rsa'.format(username)
        cmd = "ssh-keygen -q -t rsa -N '' -f {}".format(keyfile)
        conn.sudo(cmd)
