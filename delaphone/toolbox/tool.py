class Tool:
    def __init__(self, **kwargs):
        if 'host' in kwargs:
            from delaphone.toolbox.remote import RemoteHost
            self.handler = RemoteHost(**kwargs)
        else:
            from delaphone.toolbox.localhost import Localhost
            self.handler = Localhost(**kwargs)
