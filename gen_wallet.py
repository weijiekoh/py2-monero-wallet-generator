#!/usr/bin/env python

from moneropy import account

seed, sk, vk, addr = account.gen_new_wallet()

print "Public Monero address:"
print addr
print
print("DO NOT SHARE THE INFORMATION BELOW OR YOU WILL LOSE YOUR FUNDS:")
print
print "Private memonic seed:"
i = 1
for word in seed:
    print word,
    if i % 10 == 0:
        print
    i += 1

print
print
print "Private spend key"
print sk
print
print "Private view key"
print vk
