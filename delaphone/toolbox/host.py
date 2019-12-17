import os
from getpass import getuser

class SystemNotDetected: pass
class CommandNotFound: pass
class MissingPassword: pass

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
        if os.path.isfile("/etc/fedora-release"):
            from delaphone.toolbox.system.fedora import Fedora
            return Fedora(self)
        else:
            raise SystemNotDetected()
