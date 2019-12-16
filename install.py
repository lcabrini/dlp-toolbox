#! /usr/bin/env python3

import os
import log
from delaphone.toolbox.util import *

toolbox_home = "/usr/local/delaphone/toolbox"

sudo_password = inputpw("Enter your password")

if os.path.isdir(toolbox_home):
    pass
else:
    # TODO: create the directory here.
    pass
