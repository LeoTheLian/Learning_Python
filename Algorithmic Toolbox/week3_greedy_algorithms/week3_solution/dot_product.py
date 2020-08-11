#Uses python3

import sys
import random

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(0, len(a)):
        res += sorted(a)[i] * sorted(b)[i]
    return res



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    # a = [random.randint(-10**5, 10**5)] * 1000
    # b = [random.randint(-10**5, 10**5)] * 1000
    print(max_dot_product(a, b))
    
