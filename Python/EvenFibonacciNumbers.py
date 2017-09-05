#!/usr/local/bin/python3.6

total = 0
current = 2
previous = 1
tmp = 0

while (current < 4000000):
    if (current % 2 == 0):
        total += current
    tmp = previous
    previous = current
    current = current + tmp

print(total)
