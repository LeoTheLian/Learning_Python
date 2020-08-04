# Uses python3
import numpy as np

def edit_distance(s, t):
    rows, cols = (len(s) + 1, len(t) + 1)
    distance = np.array([[0] * cols] * rows)

    # set first row and first column
    distance[0, :] = np.array([range(0, cols)])
    distance[:, 0] = np.array([range(0, rows)])


    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insertion = distance[i, j - 1] + 1
            deletion = distance[i - 1, j] + 1
            match = distance[i - 1, j - 1]
            mismatch = distance[i - 1, j - 1] + 1
            if s[i - 1] == t[j - 1]:
                distance[i, j] = min(insertion, deletion, match)
            else:
                distance[i, j] = min(insertion, deletion, mismatch)
    return distance[len(s), len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
