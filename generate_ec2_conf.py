#!/usr/bin/env python3

"""
Generate a masscan configuration file for the AWS EC2 IP ranges. Always make
sure you use the masscan exclude.conf file when scanning AWS because some of
the IP ranges should be excluded from scanning. You should periodically do a
git pull of the masscan github repository to get the latest exclude.conf file.
"""
import requests

RATE = 5000.00
OUTFILE = 'ec2.list'
PORT = '6379'

resp = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
ranges = resp.json()

ec2 = [r['ip_prefix'] for r in ranges['prefixes'] if r['service'] == 'EC2']

with open('ec2.conf', 'wb') as f:
    f.write('# EC2 Masscan Configuration.\n'.encode('utf-8'))
    f.write('rate = {0}\n'.format(RATE).encode('utf-8'))
    f.write('output-format = list\n'.encode('utf-8'))
    f.write('output-filename = {0}\n'.format(OUTFILE).encode('utf-8'))
    f.write('port = {0}\n'.format(PORT).encode('utf-8'))
    f.write('exclude-file = exclude.conf\n'.encode('utf-8'))
    for r in ec2:
        f.write('range = {0}\n'.format(r).encode('utf-8'))
