if __name__ == '__main__':
    n = int(input())

    
    if 1 <= n <= 20:
    
        for i in range(n):
            print(i**2)
    else:
        print("n must be between 1 and 20")
