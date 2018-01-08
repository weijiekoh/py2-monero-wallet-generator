# py2-monero-wallet-generator

This script generates a new Monero wallet and displays the address, memonic
seed, private view key, and private spend key.

It is a pure Python 2 script and is meant for the Raspberry Pi, but can work on
any machine that runs Python 2.

I created this for use within
[malvarma](https://github.com/weijiekoh/malvarma), a secure cold wallet
generator for the truly paranoid.

This script can only generate a cold wallet if it is run in a secure
environment. If you use this script to generate an address on an insecure or
non-airgapped computer, treat it as a cold wallet at your own risk.

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

## Technical details

py2-monero-wallet-generator runs a modified version of
[bigreddmachine](https://github.com/bigreddmachine)'s
[MoneroPy](https://github.com/bigreddmachine/MoneroPy). The only change I made
to the MoneroPy is to swap out the `sha3` function with
[python-sha3](https://github.com/moshekaplan/python-sha3), a pure-Python SHA3
implementation written by [Moshe Kaplan](https://github.com/moshekaplan).
I did this because the alternative would be to cross-compile the Monero source
code for the Raspberry Pi.

The difference between this version of Moneropy and the original is as such:

```diff
13c13
< import python_sha3
---
> import sha3
27c27
<     k = python_sha3.sha3_256()
---
>     k = sha3.keccak_256()
```

## Legalese

MoneroPy is licensed under the BSD-3-Clause license and its copyright notice is as follows:

```
BSD 3-Clause License

Copyright (c) 2016 The MoneroPy Developers.
All rights reserved.
```

py2-monero-wallet-generator is licensed under the MIT License, but this license
only applies to the code in `gen_wallet.py`, and not the code from python-sha3
or MoneroPy.
