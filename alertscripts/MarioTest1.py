#!/home/docker/anaconda3/bin/python
# -*- coding: utf-8 -*-

'''
# MarioTest1.py
'''

import telegram
import sys

def Send_TG(title,body):
    lst = []
    lst.append(title)
    lst.append(body)
    # x = "%s\n%s" %  (title % body)
    bot = telegram.Bot(token='268166352:AAFxzitvTUAdlrVyhJ0B4PxCflZiuXRPoUo')
    bot.sendMessage(chat_id="-1001087174851", text="\n".join(lst))

if __name__ == '__main__':

    t1 = sys.argv[1]
    t2 = sys.argv[2]
    t3 = sys.argv[3]
    data = {"t1":t1,"t2":t2,"t3":t3}

    Send_TG(t2,t3)
