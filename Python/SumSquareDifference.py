#!/usr/local/bin/python3.6

if __name__ == '__main__':
    norm_sum = 0
    square_sum = 0

    for i in range(1,101):
        norm_sum += i
        square_sum += i**2

    print(abs(square_sum - norm_sum**2))
