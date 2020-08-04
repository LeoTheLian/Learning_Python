# Uses python3
import sys

def get_majority_element(a, left, right):
    freq = {}
    for i in a:
        if i not in freq.keys():
            freq[i] = 0
    for i in a:
        freq[i] += 1

    if max(freq.values()) > len(a)/2:
        return 1
    else:
        return 0  


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

print(get_majority_element(a, 0, n))

