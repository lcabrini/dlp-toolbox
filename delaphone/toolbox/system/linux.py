class Linux:
    def __init__(self, host):
        self.host = host

    def file_exists(self, path):
        cmd = "test -f {}".format(path)
        ret, out, err = self.host.run(cmd)
        return ret == 0

    def ls(self, path):
        cmd = "/bin/ls {}".format(path)
        ret, out, err = self.host.run(cmd)
        if ret == 0:
            return out

    def tail_messages(self):
        cmd = 'tail -n 10 /var/log/messages'
        ret, out, err = self.host.sudo(cmd)
        if ret == 0:
            return out
        else:
            # TODO: raise an error?
            return err

    def deploy(self):
        pass
