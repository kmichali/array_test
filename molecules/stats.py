#!/usr/bin/env python2

import os
import sys


fin = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
for line in fin:
     fout.write(line)

fin.close()
fout.close()
     


