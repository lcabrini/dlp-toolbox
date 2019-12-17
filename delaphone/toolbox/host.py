# Copyright 2019 Lorenzo Cabrini
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import os
from getpass import getuser
from delaphone.toolbox.system.linux import Linux

import coloredlogs, logging
# TODO: this configuration should not be here.
#logging.basicConfig(format="%(levelname)s: %(message)s",
#        level=logging.INFO)
log = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=log)

class SystemNotDetected(Exception): pass
class NoSuchCommand(Exception): pass
class MissingPassword(Exception): pass

class Host:
    """ 
    A host is a machine on a network. There are two types of host: local
    and remote. This class is a base class for *Localhost* and 
    *RemoteHost*.

    You will normally not create a Host directory. Use the get_host
    function instead."
    """

    def __init__(self, **kwargs):
        """
        Refer to the Localhost and RemoteHost documentation for details
        on which kwargs are important to those classes.
        """

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
        """
        Detects the type of system that this host is running and return
        an object representing that system (with a reference to this
        host).

        If the host cannot be detected, it returns a generic Linux 
        object.
        """

        # TODO: this is acceptable for now, since we are only working with
        # Linux systems. Later I may need a different base class here.
        linux = Linux(self)

        if linux.file_exists("/etc/fedora-release"):
            log.debug("detected Fedora on %s.", self)
            from delaphone.toolbox.system.fedora import Fedora
            return Fedora(self)
        elif linux.file_exists("/etc/issabel.conf"):
            log.debug("detected Issabel on %s", self)
            from delaphone.toolbox.system.issabel import Issabel
            return Issabel(self)
        else:
            log.warn("failed to detect OS on %s, using generic Linux", 
                    self)
            return linux
            #raise SystemNotDetected()

def get_host(**kwargs):
    """ 
    Returns a host object embedded in a Linux object, which leads to the
    obvious question: if this function doesn't return a Host object, why
    is it called get_host()? This is a good question. I wrote this code
    and I honestly don't have a clue.
    """

    if 'host' in kwargs and not kwargs['host'] is None:
        log.debug("connecting to remote host: %s", kwargs['host'])
        from delaphone.toolbox.remote import RemoteHost
        return RemoteHost(**kwargs).detect()
    else:
        log.debug("working on localhost")
        from delaphone.toolbox.localhost import Localhost
        return Localhost(**kwargs).detect()
