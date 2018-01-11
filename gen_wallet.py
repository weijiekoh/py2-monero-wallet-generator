#!/usr/bin/env python

from moneropy import account

seed, sk, vk, addr = account.gen_new_wallet()

print "Copy the address, memonic seed & private keys exactly as shown. Store them safely."
print "Public Monero address:", addr
print("NOTE: DO NOT SHARE THE INFO BELOW OR YOU WILL LOSE YOUR FUNDS:")
print "Private memonic seed:"
i = 1
for word in seed:
    print word,
    if i % 10 == 0:
        print
    i += 1

print
print "Private spend key:", sk
print "Private view key:", vk
