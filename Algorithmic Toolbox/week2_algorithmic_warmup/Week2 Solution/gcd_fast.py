def get_gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    rem = max(a, b) % min(a, b)
    return get_gcd(rem, min(a,b))

if __name__ == '__main__':
    a, b = input().split(' ')
    print(get_gcd(int(a), int(b)))