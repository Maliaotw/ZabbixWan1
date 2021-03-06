#!/home/docker/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
Zabbix SMTP Alert script for gmail.
"""
import sys
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
# Mail Account
MAIL_ACCOUNT = 'it1.wonderful@gmail.com'
MAIL_PASSWORD = '4rfvgy7u'
# Sender Name
SENDER_NAME = u'Zabbix Server Alert'
# Mail Server
SMTP_SERVER = 'smtp.gmail.com'

#SMTP_PORT = 465
SMTP_PORT = 587
# TLS

SMTP_TLS = True
SMTP_SSL = True


def send_mail(recipient, subject, body, encoding='utf-8'):

    session = None

    msg = MIMEText(body, 'plain', encoding)

    msg['Subject'] = Header(subject, encoding)

    msg['From'] = Header(SENDER_NAME, encoding)

    msg['To'] = recipient

    msg['Date'] = formatdate()

    try:

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        if SMTP_TLS:

            session.ehlo()

            session.starttls()

            session.ehlo()

            session.login(MAIL_ACCOUNT, MAIL_PASSWORD)

        session.sendmail(MAIL_ACCOUNT, recipient, msg.as_string())

    except Exception as e:

        raise e

    finally:

        # close session

        if session:

            session.quit()



if __name__ == '__main__':

    try:
        send_mail(recipient=sys.argv[1],subject=sys.argv[2],body=sys.argv[3])
    except:
        print "Error"
