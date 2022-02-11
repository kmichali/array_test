# averages values in all pi.* files made by pi_mc.py

import statistics
import os

os.system('cat pi.* > pi.txt')

with open('pi.txt') as f:
    lines = f.readlines()

numbers = [float(line.strip()) for line in lines[:-1]]
print(statistics.mean(numbers))


