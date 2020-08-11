# Uses python3
import sys

def get_change(m):
    n = 0 # number of changes
    while m > 0:
        if m >= 10:
            m -= 10
            n += 1
            continue
        if m < 10 and m >= 5:
            m -= 5
            n += 1
            continue
        if m < 5:
            m -= 1
            n += 1
            continue
    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
