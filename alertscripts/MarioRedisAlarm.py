#!/home/docker/anaconda2/bin/python
# -*- coding: utf-8 -*-
'''
# MarioRedisAlarm.py
'''
import sys
import redis
import os

if __name__ == '__main__':
    rc = redis.StrictRedis("192.168.8.22")
    status = sys.argv[2].decode('utf8')
    name = sys.argv[3].decode('utf8')

    # dict1 = {name: status}

    if "OK" in status:
        # rc.hmset("Zabbix", dict1)
        rc.set(name,status)
    else:
        # rc.hmset("Zabbix", dict1)
        rc.set(name,status)
        # os.system("curl --user wonderful:08d6aacb79bfd94f548379ab928d7fba 192.168.8.22:8081/jenkins/view/PC-054/job/PC-054_ErrorWave/build?token=wonderful")
