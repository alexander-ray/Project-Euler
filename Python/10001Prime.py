#!/usr/local/bin/python3.6

def is_prime(test):
    for i in range(2,int(test**.5)+1):
        if (test % i == 0):
            return False
    return True

def main():
    counter = 1
    num = 1
    while counter < 10002:
        num += 1
        if (is_prime(num)):
            counter += 1

    print(num)

if __name__ == '__main__':
    main()
