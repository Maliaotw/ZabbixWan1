#!/home/docker/anaconda2/bin/python
# -*- coding: utf-8 -*-
'''
# MarioAlarmTG.py
'''

import telegram
import sys

def Send_TG(ID,title,body):
    x = title +"\n"+ body
    bot = telegram.Bot(token='220850856:AAHiNurnEPewri8_iFLe3E23JTzAYJO7UXs')
    bot.sendMessage(chat_id=ID, text=x)

if __name__ == '__main__':

    tt = sys.argv[2].decode('utf8')
    bb = sys.argv[3].decode('utf8')
    Send_TG(sys.argv[1],tt,bb)
