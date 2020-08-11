# python3
# Find the largest pairwise product in a list


def max_pairwise_product(numbers):
    n = len(numbers)
    max_index1 = 0
    max_index2 = 0

    if n == 2:
        return numbers[0] * numbers[1]

    for i in range(n):
        if (max_index1 == 0) or (numbers[i] >= numbers[max_index1]):
            max_index1 = i

    for j in range(n):
        if ((max_index2 == 0) or (numbers[j] >= numbers[max_index2])) and (j != max_index1):
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
