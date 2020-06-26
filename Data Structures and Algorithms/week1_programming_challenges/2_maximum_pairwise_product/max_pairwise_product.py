# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = 0
    max2 = 0
    for i in range(n):
        max1 = max(max1,numbers[i])
        max1_index = numbers.index(max1)
    for i in range(n-1):

    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
