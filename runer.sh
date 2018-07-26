#!/bin/sh
python EmailHarvester.py -d $1 -e all -l 50 -s emails.txt && python grabclean.py | python pwnedornot.py -f out.txt
