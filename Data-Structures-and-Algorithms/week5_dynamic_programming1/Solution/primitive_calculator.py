# Uses python3
import sys

def optimal_sequence(n):
    min_op = [0] * (n+1)
    min_op[1] = 1
    for i in range(2, n+1):
        # reachable indices
        indices = [i-1]
        if i % 2 == 0:
            indices.append(i//2)
        if i % 3 == 0:
            indices.append(i//3)
    
        operation = min(min_op[x] for x in indices)
        min_op[i] = operation + 1

    current_num = n
    sequence = [current_num]
    while current_num > 1:
        partition = [current_num - 1]
        if current_num % 2 == 0:
            partition.append(current_num // 2)
        if current_num % 3 == 0:
            partition.append(current_num // 3)

        current_num = min([(p, min_op[p]) for p in partition], key = lambda x: x[1])[0]
        sequence.append(current_num)
    
    return list(reversed(sequence))



input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
