#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

def banner():
    print('\n%s v 1.0\nby d2@tdhack.com\n' % sys.argv[0])

def getlength(fname):
    return sum(1 for line in open(fname))

def ifexist(fname):
    if not os.path.isfile(fname):
        banner()
        print('[-] %s must exist' % fname)
        sys.exit(1)

def replace(l, X, Y):
  for i,v in enumerate(l):
     if v == X:
        l.pop(i)
        l.insert(i, Y)

if len(sys.argv) < 2:
    banner()
    print('[-] please provide CRACKED and HASHES files')
    sys.exit(1)

CRACKED=sys.argv[1]
HASHES=sys.argv[2]

ifexist(CRACKED)
ifexist(HASHES)

banner()
print('[i] preparing lists from "%s" [%d lines] and "%s" [%d lines]' %(CRACKED, getlength(CRACKED), HASHES, getlength(HASHES)))
with open(CRACKED) as crackedfile:
    cracked = dict(map(str, line.split(':', 1)) for line in crackedfile if ':' in line)

hashdata = [line.rstrip('\n') for line in open(HASHES)]

print('[i] pairing items, this will take a while so please be patient')
for item in hashdata:
    if item in cracked:
        replace(hashdata, item, item+':'+cracked[item].strip('\n'))

print('[i] writting changes')
fout = open(HASHES+'_paired', 'w')
for item in hashdata:
    fout.write(item+'\n')
fout.close()

print('[+] done, now check "%s" [%d lines] file for results.' % (HASHES+'_paired', getlength(HASHES+'_paired')))
