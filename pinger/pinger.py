#! /usr/bin/env python3

#import shlex
#import subprocess
import time
import threading
import schedule
import pingparsing
import config

def ping(host):
    parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 5
    result = transmitter.ping()
    stats = parser.parse(result).as_dict()
    print(stats['rtt_avg'])
    #print(json.dumps(parser.parse(result).as_dict(), indent=2))
    #cmd = "ping -c 5 {}".format(ip)
    #args = shlex.split(cmd)
    #proc = subprocess.run(args, capture_output=True)
    #for line in proc.stdout.splitlines()[-2:]:
    #    s = line.decode("UTF-8")
    #    print(s)
    #    #pass
    #    #print("LINE: {}".format(line.decode("UTF-8")))

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
