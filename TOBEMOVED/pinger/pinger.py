#! /usr/bin/env python3

import time
import threading
import requests
import schedule
import pingparsing
import config

def sms(msg):
    url = "http://{}/bulksms/bulksms".format(config.SMS['url'])
    destination = ','.join(config.SMS['recipients'])
    #for recipient in config.SMS['recipients']:
    #print("recp: {}".format(recipient))
    params = {
            "username": config.SMS['username'],
            "password": config.SMS['password'],
            "type": "0",
            "dlr": "1",
            "destination": destination,
            "source": "Delaphone",
            "message": str(msg),
            }
    resp = requests.get(url, params=params)
    print("SMS: to {}, resp: {}".format(destination, resp))

def ping(host):
    #print(host)
    parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 5
    result = transmitter.ping()
    if result.returncode != 0:
        message = """This is a test message. Ping {}, down.
        """.format(host)
        sms(message)
    else:
        #print(result)
        parser.parse(result)
        stats = parser.as_dict()
        #print(stats['packet_loss_count'])
        if stats['packet_loss_count'] > 0:
            message = """This is a test message. Ping {}, packet loss.
            """.format(stats['destination'])
            sms(message)

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
