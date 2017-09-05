#!/usr/local/bin/python3.6

def is_palindrome(num):
    s = str(num)
    split = -((-len(s)) // 2)
    first, second = s[:split], s[split:]

    # Extended slice syntax ([being:end:step])
    # Reverses string
    second = second[::-1]
    
    if (first == second):
        return True
    else:
        return False

if __name__ == '__main__':
    current_largest = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j) and i*j > current_largest:
                current_largest = i*j

    print(current_largest)
