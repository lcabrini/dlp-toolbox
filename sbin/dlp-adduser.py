#! /usr/bin/python3

import sys
import os

if os.geteuid() == 0:
    print("This program should not be run as root")
    sys.exit(1)
    
