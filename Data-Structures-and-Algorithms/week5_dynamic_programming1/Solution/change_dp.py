# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    min_change = [-1] * (m+1)
    min_change[0] = 0 # 0 money = 0 change
    for i in range(1, m+1):
        for coin in coins:
            if coin <= i:
                if min_change[i - coin] + 1 < min_change[i] or min_change[i] < 0:
                    min_change[i] = min_change[i - coin] + 1
    return min_change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
