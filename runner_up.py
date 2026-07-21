if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    highest = -1000

    for score in arr:
        if score > highest:
            highest = score

    runner_up = -100

    
            
    for score in arr:
        if score != highest and score > runner_up:
            runner_up = score

    print(runner_up)
