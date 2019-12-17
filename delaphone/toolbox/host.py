from getpass import getuser

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

