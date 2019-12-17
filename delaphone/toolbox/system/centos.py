from delaphone.toolbox.system.linux import Linux

class CentOS(Linux):
    def __init__(self, host):
        super().__init__(host)
        print("CentOS")
