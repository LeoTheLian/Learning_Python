# An improved algorithm for Fibonacci Sequence
# input: n
# output n-th number in the Fibonacci Sequence


def calc_fib(n):
    if n<=1:
        return n
    fibo = [0]*n
    fibo[0] = 1
    fibo[1] = 1
    for i in range(2,n):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n-1]


n = int(input())
print(calc_fib(n))