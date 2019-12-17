from delaphone.toolbox.localhost import Localhost
from delaphone.toolbox.remote import RemoteHost

class Tool:
    def __init__(self, **kwargs):
        if 'host' in kwargs:
            self.handler = RemoteHost(kwargs)
        else:
            self.handler = Localhost(kwargs)
