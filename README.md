# About

Set of Python scripts to manage wordlists.

* **item_pairing.py** - pair items from two lists. First list contains hashes, second hash:plaintext pairs. The goal here is to update 'hashes' with corresponding plaintext passwords without changing order of hashes. This script assumes '\n' as EOL.

### Requirements

* python with modules 'os' and 'sys'

;-)

### Example outputs:
```
# time python item_pairing.py 64k-md5_found.txt 64k-md5.txt

item_pairing.py v 1.0
by d2@tdhack.com

[i] preparing lists from "64k-md5_found.txt" [39796 lines] and "64k-md5.txt" [64015 lines]
[i] pairing items
[i] writting changes
[+] done, now check "64k-md5.txt_paired" [64015 lines] file for results.

real    2m25.789s
user    2m25.180s
sys     0m0.560s
```
### installation
No special instructions, just make sure your python is working.

### todo
* autodetect EOL, convert it to '\n'

### Ideas? Reports?

Send them to: d2@tdhack.com
