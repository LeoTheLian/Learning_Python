# Uses python3


def get_fibonacci_last_digit_fast(n):
    previous = 0
    current  = 1
    if n > 60:
        n %= 60
    
    if n <= 1:
        return n
    
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
