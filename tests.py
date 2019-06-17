#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker
import requests

client = docker.from_env()

time.sleep(20)

for c in client.containers.list():
    print(c.name)
    print(c.status)
    if 'running' not in c.status:
        print(c.logs())

# NGINX
nginx = client.containers.get('nginx')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
# print(nginx_cfg.output.decode())
assert 'server_name _;' in nginx_cfg.output.decode()
assert "error_log /proc/self/fd/2" in nginx_cfg.output.decode()
assert "location = /.well-known/acme-challenge/" in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()

# test restart
nginx.restart()
time.sleep(3)
assert nginx.status == 'running'

# Symfony PHP
php = client.containers.get('registry')
assert php.status == 'running'
# print(php_conf.output.decode())
response = requests.get("http://localhost")
assert response.status_code == 200
print(response.text)
assert 'Welcome to the famous five-minute registry installation process!' in response.text
