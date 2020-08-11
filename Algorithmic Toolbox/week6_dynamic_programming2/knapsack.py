# Uses python3
import sys
import numpy as np 
def optimal_weight(W, w):
    n = len(w)
    # initialize matrix (n*W) with -1
    value = np.array([[-1] * (W + 1)] * (n + 1))
    

    # Capacity = 0 -> total weight always 0
    # items = 0 -> total weight always 0
    value[0,:] = 0
    value[:,0] = 0
    
    for item in range(1, n + 1):
        for weight in range(1, W + 1):
            value[item, weight] = value[item - 1, weight]
            if w[item - 1] <= weight:
                val = value[item - 1, weight - w[item - 1]] + w[item - 1]
                if value[item, weight] < val:
                    value[item, weight] = val
    return value[n, W]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
