import configparser
import requests

# TODO: don't hardcode config file
config = configparser.ConfigParser()
config.read('etc/delaphone.ini')

def routesms_send(destination, message):
    url = config['sms']['url']
    params = {
            "username": config['sms']['username'],
            "password": config['sms']['password'],
            "type": "0",
            "dlr": "1",
            "destination": destination,
            "source": config['sms']['source'],
            "message": message
            }
    requests.get(url, params=params)
    # TODO: get status code from RouteSMS
