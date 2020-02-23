def get_sum(z, y):
    sum = 0

    for x in range(z, y, 1):
        sum = sum + x

    print(sum)

    return sum


a = 3
b = 7
get_sum(a, b)
