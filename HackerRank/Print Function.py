if __name__ == '__main__':
    n = int(input())
    result = 0
    multiplier = 1

    for i in range(1, n + 1):
        digits = len(str(i))
        result = result * (10 ** digits) + i

    print(result)
