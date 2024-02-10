if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # Convert into tuple
    t = tuple(integer_list)
    
    print(hash(t))
