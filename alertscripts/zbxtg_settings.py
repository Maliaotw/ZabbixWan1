#!/home/docker/anaconda2/bin/python
# -*- coding: utf8-*-

tg_key = "220850856:AAHiNurnEPewri8_iFLe3E23JTzAYJO7UXs"  # telegram bot api key

zbx_tg_prefix = "zbxtg.py"###  # variable for separating text from script info
zbx_tg_tmp_dir = "/tg/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_server = "http://192.168.8.28/"  # zabbix server full url
zbx_api_user = "admin"
zbx_api_pass = "zabbix"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

proxy_to_zbx = None
proxy_to_tg = None

#proxy_to_zbx = "proxy.local:3128"
#proxy_to_tg = "proxy.local:3128"

emoji_map = {
    "ok": "✅",
    "problem": "❗",
    "info": "ℹ️",
    "warning": "⚠️",
    "disaster": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
