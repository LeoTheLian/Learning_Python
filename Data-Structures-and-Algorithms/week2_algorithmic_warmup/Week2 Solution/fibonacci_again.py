def fibo_again(n, m):
    fibo = [0,1]
    rem = [0,1]
    
    match = False
    p = 2
    while not match:
        fibo.append(fibo[p-1] + fibo[p-2])
        rem.append(fibo[p] % m)
        if rem[p-1] == 0 and rem[p] == 1:
            match = True
            period = p-1
        p += 1            
    rem = rem[:-2]
    return rem[n%period]



if __name__ == '__main__':
    n, m = input().split(' ')
    print(fibo_again(int(n), int(m)))