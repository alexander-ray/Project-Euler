#!/usr/local/bin/python3.6

def is_prime(test):
    for i in range(2,int(test**.5)+1):
        if (test % i == 0):
            return False
    return True


if __name__ == '__main__':
    num = 600851475143
    test = 3
    current_largest = 0

    while (current_largest < (num / 2)):
        if (is_prime(test) and test > current_largest and num % test == 0):
            current_largest = test
            num /= current_largest
        test += 1

    print(current_largest)
