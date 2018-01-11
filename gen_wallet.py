#!/usr/bin/env python
import os
import sys

from moneropy import account

seed, sk, vk, addr = account.gen_new_wallet()

if len(sys.argv) > 1 and sys.argv[1] == "--clear":
    os.system('clear')

print "Copy the following text exactly as shown and store it offline:"
print "Public Monero address:", addr
print("NOTE: DO NOT SHARE THE INFO BELOW OR YOU WILL LOSE YOUR FUNDS:")
print "Private spend key:", sk
print "Private view key: ", vk
print "Private mnemonic seed:"
i = 1
for word in seed:
    print word,
    if i % 10 == 0:
        print
    i += 1
print
