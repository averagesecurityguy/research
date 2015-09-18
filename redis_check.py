#!/usr/bin/env python3

import sys
import redis
import redis.exceptions

host = sys.argv[1]
host = host.strip('\r\n')
port = 6379
timeout = 5

try:
    db = redis.StrictRedis(host=host, port=port, socket_timeout=timeout)
    i = db.info()
    ver = i.get('redis_version')
    siz = db.dbsize()
   
    print('[+] {0}:{1}:{2}'.format(host, ver, siz))

except redis.exceptions.ResponseError as e:
    print('[+] {0}::{1}'.format(host, e))

except redis.exceptions.ConnectionError:
    print('[-] {0}::Connection Error'.format(host))

except redis.exceptions.TimeoutError:
    print('[-] {0}::Timeout'.format(host))

except redis.exceptions.InvalidResponse:
    print('[-] {0}::Invalid Response'.format(host))
