#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while a:
        max_digit = a[0]
        for digit in a:
            if is_greater(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    return res
            
def is_greater(d, m):
    d_plus_m = int(d + m)
    m_plus_d = int(m + d)
    if d_plus_m >= m_plus_d:
        return True
    else:
        return False

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    
    
