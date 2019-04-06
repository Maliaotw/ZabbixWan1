# 建置筆記

**Clone Project**

```
cd ~
mkdir workspace
cd ~/workspace
git clone http://gitlab.example.com/Docker/ZabbixWan1.git
```

**docker-compose.yaml**

```
version: '2'
services:
  zabbix-server:
    labels:
      io.rancher.scheduler.global: 'true'
      io.rancher.scheduler.affinity:host_label: name=ZabbixWan1
    image: monitoringartist/zabbix-xxl:latest
    environment:
      ZS_DBHost: zabbix.db
      ZS_DBPassword: admin
      ZS_DBUser: zabbix
    volumes:
    - /etc/localtime:/etc/localtime:ro
    - /home/docker1/workspace/ZabbixWan1/temp:/usr/local/src/zabbix/temp
    - /home/docker1/workspace/ZabbixWan1/conf/fonts/:/usr/local/src/zabbix/frontends/php/fonts/
    - /home/docker1/workspace/ZabbixWan1/conf/defines.inc.php:/usr/local/src/zabbix/frontends/php/include/defines.inc.php
    - /home/docker1/workspace/ZabbixWan1/conf/alertscripts:/usr/local/share/zabbix/alertscripts
    links:
    - zabbix-db:zabbix.db
    ports:
    - 80:80/tcp
    - 10051:10051/tcp
  zabbix-db:
    labels:
      io.rancher.scheduler.global: 'true'
      io.rancher.scheduler.affinity:host_label: name=ZabbixWan1
    image: monitoringartist/zabbix-db-mariadb
    environment:
      MARIADB_PASS: admin
      MARIADB_USER: zabbix
    volumes:
    - /home/docker1/workspace/ZabbixWan1/zabbix-db-storage:/var/lib/mysql
    - /home/docker1/workspace/ZabbixWan1/backups:/backups
    - /etc/localtime:/etc/localtime:ro
    ports:
    - 3306:3306/tcp

```