# py2-monero-wallet-generator

This script generates a new Monero wallet and displays the address, memonic
seed, private view key, and private spend key.

It is a pure Python 2 script and is meant for the Raspberry Pi.

It runs a modified version of
[bigreddmachine](https://github.com/bigreddmachine)'s
[MoneroPy](https://github.com/bigreddmachine/MoneroPy). The only change I made
to the MoneroPy is to swap out the `sha3` function with
[python-sha3](https://github.com/moshekaplan/python-sha3), a pure-Python SHA3
implementation written by [Moshe Kaplan](https://github.com/moshekaplan).

The difference between this version of Moneropy and the original is as such:

```diff
moneropy/cryptonote.py
< import python_sha3
---
> import sha3
py2-monero-wallet-generator/moneropy/cryptonote.py
<     k = python_sha3.sha3_256()
---
>     k = sha3.keccak_256()
```

## Usage

```bash
git clone git@github.com:weijiekoh/py2-monero-wallet-generator.git && \
cd py2-monero-wallet-generator && \
python gen_wallet.py
```

Output:

```
Public Monero address:
4At..........................................................................................ev

DO NOT SHARE THE INFORMATION BELOW OR YOU WILL LOSE YOUR FUNDS:

Private memonic seed:
blah blah blah blah blah blah blah blah blah blah 
blah blah blah blah blah blah blah blah blah blah 
blah blah blah blah

Private spend key
a..............................................................6

Private view key
d..............................................................1
```
