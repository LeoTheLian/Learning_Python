def get_sum_squared(n):
    
    fibo = [0]*3
    fibo[0] = 1
    fibo[1] = 1
    fibo[2] = fibo[0] + fibo[1]
    
    if n > 60:
        n %= 60
       
    if n <= 1:
        return n

    for i in range(2, n+1):
        next_num = fibo[1] + fibo[2]
        fibo[0] = fibo[1]
        fibo[1] = fibo[2]
        fibo[2] = next_num
    return ((fibo[0] % 10) * (fibo[1] % 10)) % 10


if __name__ == '__main__':
    n = int(input())
    print(get_sum_squared(n))
