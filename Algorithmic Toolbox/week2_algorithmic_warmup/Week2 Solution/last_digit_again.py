def get_sum_again(m, n):
   
    fibo = [0]*3
    fibo[0] = 1
    fibo[1] = 1
    fibo[2] = fibo[0] + fibo[1]
    sum_m = 0
    sum_n = 0
    
    if n > 60:
        n %= 60
    
    if m > 60:
        m %= 60
    
    if n <= 1:
        return n
    
    if n < m:
        n += 60
    
    for i in range(2, n+1):
        next_num = fibo[1] + fibo[2]
        fibo[0] = fibo[1]
        fibo[1] = fibo[2]
        fibo[2] = next_num

        if i == m:
            sum_m = (fibo[1] - 1) % 10
    
    sum_n = (fibo[2]-1) % 10

    if sum_n < sum_m:       
        return sum_n+10-sum_m
    
    else:
        return sum_n - sum_m


if __name__ == '__main__':
    m, n = input().split(' ')
    print(get_sum_again(int(m), int(n)))