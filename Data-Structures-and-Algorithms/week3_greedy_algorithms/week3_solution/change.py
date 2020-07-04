# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    while m > 0:
        if m >= 10:
            m -= 10
            count += 1
            continue
        if m < 10 and m >= 5:
            m -= 5
            count += 1
            continue
        if m < 5:
            m -= 1
            count += 1
            continue
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
