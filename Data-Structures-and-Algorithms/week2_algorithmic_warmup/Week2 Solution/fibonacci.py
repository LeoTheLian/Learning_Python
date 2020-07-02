# Uses python3
def get_fibo(n):
    if n <= 1:
        return n
    fibo = [0] * n
    fibo[0] = 1
    fibo[1] = 1
    for i in range(2, n):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo


for i in range (2, 50):
    print(str(sum(get_fibo(i)))[-1])
