#!/usr/local/bin/python3.6

def is_divisible(num):
    for i in range(1,21):
        if (num % i != 0):
            return False

    return True

if __name__ == '__main__':
    num = 20
    while True:
        if (is_divisible(num)):
            print(num)
            break
        else:
            num += 10
