def get_lcm(a, b):
    def get_gcd(a, b):
        if b == 0:
            return a
        if a == 0:
            return b
        rem = max(a, b) % min(a, b)
        return get_gcd(rem, min(a,b))
    return int(a*b/get_gcd(a,b))


if __name__ == '__main__':
    a, b = input().split(' ')
    print(get_lcm(int(a), int(b)))