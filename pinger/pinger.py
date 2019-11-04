#! /usr/bin/env python3

import shlex
import subprocess
import time
import threading
import schedule
import config

def ping(host):
    for ip in config.HOSTS:
        cmd = "ping -c 5 {}".format(ip)
        args = shlex.split(cmd)
        proc = subprocess.run(args, capture_output=True)
        for line in proc.stdout.splitlines()[-2:]:
            s = line.decode("UTF-8")
            print(s)
            #pass
            #print("LINE: {}".format(line.decode("UTF-8")))

def ping_job():
    threads = list()
    for host in config.HOSTS:
        t = threading.Thread(target=ping, args=(host,), daemon=True)
        threads.append(t)
        t.start()
    #print("started {} threads".format(len(threads)))

schedule.every(10).seconds.do(ping_job)
while True:
    schedule.run_pending()
    time.sleep(1)
