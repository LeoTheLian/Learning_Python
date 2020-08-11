# Uses python3
import sys
import numpy as np

def partition3(A):
    # check if the items are divisible
    if sum(A) % 3 != 0:
        return 0
    # no need to proceed if less than 3 items
    if len(A) < 3:
        return 0
    
    target = sum(A) // 3
    items = len(A)

    # initialize values array (items+1) * (target+1) with -1 
    values = np.array([[-1] * (target + 1)] * (items + 1))

    # if target value is 0: no items taken for anyone
    # if no items: nothing can be taken
    values[:, 0] = 0
    values[0, :] = 0
    count = 0 # how many times we hit target value

    for t in range(1, target + 1):
        for i in range(1, items + 1):
            values[i, t] = values[i - 1, t]
            if A[i-1] <= t:
                val = values[i - 1, t - A[i-1]] + A[i-1]
                if val > values[i, t]:
                    values[i, t] = val
                if values[i, t] == target:
                    count += 1
    
    if count >= 3:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

