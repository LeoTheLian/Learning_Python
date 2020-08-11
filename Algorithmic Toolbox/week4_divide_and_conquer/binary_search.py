# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    while right >= left:
        target = int((left + right) / 2)
        if a[target] == x:
            return target
        if a[target] > x:
            right = target - 1
        if a[target] < x:
            left = target + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
