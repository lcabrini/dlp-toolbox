from delaphone.toolbox.system.centos import CentOS

class Issabel(CentOS):
    def __init__(self, host):
        super().__init__(host)
        print("issabel")
