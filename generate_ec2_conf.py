#!/usr/bin/env python3

"""
Generate a masscan configuration file for the AWS EC2 IP ranges. Always make
sure you use the masscan exclude.conf file when scanning AWS because some of
the IP ranges should be excluded from scanning. You should periodically do a
git pull of the masscan github repository to get the latest exclude.conf file.
"""
import requests

RATE = 150000.00
FORMAT = 'list'
PORT = '445'
OUTFILE = 'ec2_{0}.list'.format(PORT)
BANNER = 'false'

resp = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
ranges = resp.json()
ec2 = [r['ip_prefix'] for r in ranges['prefixes'] if r['service'] == 'EC2']

with open('ec2.conf', 'w') as f:
    f.write('# EC2 Masscan Configuration.\n')
    f.write('rate = {0}\n'.format(RATE))
    f.write('output-format = {0}\n'.format(FORMAT))
    f.write('output-filename = {0}\n'.format(OUTFILE))
    f.write('port = {0}\n'.format(PORT))
    f.write('exclude-file = exclude.conf\n')
    f.write('banners = {0}\n'.format(BANNER))
    for r in ec2:
        f.write('range = {0}\n'.format(r))
