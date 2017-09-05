#!/usr/local/bin/python3.6

def is_prime(test):
    for i in range(2,int(test**.5)+1):
        if (test % i == 0):
            return False
    return True

def main():
    num = 2000000
    counter = 10
    for i in range(6, num):
        if (i % 2 == 0) or (i % 5 == 0):
            continue
        elif (is_prime(i)):
            counter = counter + i

    print(counter)

if __name__ == '__main__':
    main()
