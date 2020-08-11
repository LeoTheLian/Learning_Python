# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    current_weight = 0
    unit_value = [values[i]/weights[i] for i in range(0, len(values))]
    while current_weight < capacity:
        if len(unit_value) < 1:
            break
        
        max_value = max(unit_value)
        item = unit_value.index(max_value)
        max_weight = weights[item]
        if max_weight <= (capacity - current_weight):
            value += max_value * max_weight
            current_weight += max_weight
            unit_value.pop(item)
            weights.pop(item)
        else:
            value += max_value * (capacity - current_weight)
            current_weight = capacity
    return float("{:.4f}".format(value))


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
