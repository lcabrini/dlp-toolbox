import smtplib
import configparser

config = configparser.ConfigParser()
config.read('etc/delaphone.ini')

message = """\
From: {}
To: {}
Subject: {}

{}
"""

def sendmail(recipients, subject, body):
    try:
        mail = message.format(config['mail']['user'],
                ', '.join(recipients), subject, body)
        server = smtplib.SMTP_SSL(config['mail']['server'], 
                config['mail']['port'])
        server.login(config['mail']['user'], config['mail']['password'])
        server.sendmail(config['mail']['user'], recipients, mail)
    except:
        print("Foo!")



sendmail(['lorenzo.cabrini@gmail.com', 'lorenzo@delaphonegh.com'],
        "Testing", "This is a test message")
