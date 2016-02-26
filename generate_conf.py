#!/usr/bin/env python3

RATE = 150000.00
FORMAT = 'list'
PORT = '445'
OUTFILE = 'internet_{0}.list'.format(PORT)
BANNER = 'false'

with open('internet.conf', 'w') as f:
    f.write('# Internet Masscan Configuration.\n')
    f.write('rate = {0}\n'.format(RATE))
    f.write('output-format = {0}\n'.format(FORMAT))
    f.write('output-filename = {0}\n'.format(OUTFILE))
    f.write('port = {0}\n'.format(PORT))
    f.write('exclude-file = exclude.conf\n')
    f.write('banners = {0}\n'.format(BANNER))
    f.write('range = 0.0.0.0/0\n')
