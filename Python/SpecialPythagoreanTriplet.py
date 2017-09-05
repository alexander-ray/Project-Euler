#!/usr/local/bin/python3.6

for a in range(1, 334):
    for b in range (a, 667):
        c = 1000 - (a + b)
        if (a**2 + b**2 == c**2) and (a + b + c == 1000):
            print(a*b*c)
