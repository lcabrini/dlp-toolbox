#! /usr/bin/env python3

import shlex
import subprocess
import time
import schedule
import config

def ping():
    for ip in config.HOSTS:
        cmd = "ping -c 5 {}".format(ip)
        args = shlex.split(cmd)
        proc = subprocess.run(args, capture_output=True)
        for line in proc.stdout.splitlines():
            print("LINE: {}".format(line))


schedule.every(10).seconds.do(ping)
while True:
    schedule.run_pending()
    time.sleep(1)
