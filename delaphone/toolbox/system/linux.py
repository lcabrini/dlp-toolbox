class CommandFailed(Exception): pass

class Linux:
    def __init__(self, host):
        self.host = host

    def file_exists(self, path):
        cmd = "test -f {}".format(path)
        ret, out, err = self.host.run(cmd)
        return ret == 0

    def directory_exists(self, path, **kwargs):
        """ 
        Checks if the directory given by path exists. Returns True if
        it does or False if it doesn't.
        """
        cmd = "test -d {}".format(path)
        ret, out, err = self._call(cmd, **kwargs)
        return ret == 0

    def ls(self, path):
        cmd = "/bin/ls {}".format(path)
        ret, out, err = self.host.run(cmd)
        if ret == 0:
            return out

    def mkdir(self, path, **kwargs):
        """
        Creates the directory *path* or raises *CommandFailed* if it
        was not possible to create the directory.
        """
        cmd = "/usr/bin/mkdir {}".format(path)
        ret, out, err = self._call(cmd, **kwargs)
        if ret != 0:
            raise CommandFailed(err)

    def tail_messages(self):
        cmd = 'tail -n 10 /var/log/messages'
        ret, out, err = self.host.sudo(cmd)
        if ret == 0:
            return out
        else:
            # TODO: raise an error?
            return err

    def _call(self, cmd, **kwargs):
        """
        Helper method for calling Linux commands. If the keyword
        argument sudo is True, then then the command will be called
        as the user specified in the 'user' keyword argument (default
        root), otherwise it will be called as the current user.
        """
        if 'sudo' in kwargs and kwargs['sudo'] is True:
            return self.host.sudo(cmd)
        else:
            return self.host.run(cmd)

    def deploy(self):
        pass
