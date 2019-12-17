import os
from getpass import getuser
from delaphone.toolbox.system.linux import Linux

class SystemNotDetected(Exception): pass
class NoSuchCommand(Exception): pass
class MissingPassword(Exception): pass

class Host:
    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            # TODO: should we raise an error instead?
            self.host = 'localhost'

        if 'username' in kwargs:
            self.username = kwargs['username']
        else:
            self.username = getuser()

        if 'password' in kwargs:
            self.password = kwargs['password']
        else:
            # TODO: should we raise an error instead?
            self.password = ''

    def detect(self):
        # TODO: this is acceptable for now, since we are only working with
        # Linux systems. Later I may need a different base class here.
        linux = Linux(self)

        if linux.file_exists("/etc/fedora-release"):
            from delaphone.toolbox.system.fedora import Fedora
            return Fedora(self)
        else:
            print("Failed to detect system, falling back to Linux")
            return linux
            #raise SystemNotDetected()

def get_host(**kwargs):
    if 'host' in kwargs and not kwargs['host'] is None:
        print("{} is a remote host".format(kwargs['host']))
        from delaphone.toolbox.remote import RemoteHost
        return RemoteHost(**kwargs).detect()
    else:
        from delaphone.toolbox.localhost import Localhost
        print("connecting to localhost")
        return Localhost(**kwargs).detect()
