
from itertools import product
from primitive_calculator import optimal_sequence
import random


for t in range(0, 10):
    n = random.randint(0,1000)
    found = False
    answer = n-1
    for k in range(1,n):
    # enumerate all sequences of operations (+1, *2, *3)
        for seq in product([0,1,2], repeat=k):
            start = 1
            for i in seq:
                if i == 0:
                    start += 1
                if i == 1:
                    start *= 2
                if i == 2:
                    start *= 3
            # if a sequence leads to n update the answer
            if (not found) and (start == n):
                found = True
                answer = k
        if found:
            break
    print('Test', t, ':', n, len(optimal_sequence(n))-1 == answer)  