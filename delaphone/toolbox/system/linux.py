class Linux:
    def __init__(self, host):
        self.host = host

    def file_exists(self, path):
        cmd = "test -f {}".format(path)
        ret, out, err = self.host.run(cmd)
        return ret == 0
