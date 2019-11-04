#! /usr/bin/env python3

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

def ping_job():
    threads = list()
    for host in config.HOSTS:
        t = threading.Thread(target=ping, args=(host,), daemon=True)
        threads.append(t)
        t.start()

schedule.every(10).seconds.do(ping_job)
while True:
    schedule.run_pending()
    time.sleep(1)
