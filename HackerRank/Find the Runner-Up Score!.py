if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    
    scores = set(arr)
    
    
    sorted_scores = sorted(scores)

    
    runner_up_score = sorted_scores[-2]

    print(runner_up_score)
