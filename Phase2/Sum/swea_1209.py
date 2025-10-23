import sys

sys.stdin = open("input.txt","r")

T = 10

for test_case in range(1,T+1):
    input()
    arr = []
    for _ in range(100):
        arr.append(list(map(int,input().split())))

    mx = 0

    # 가로합
    for r in range(100):
        tmp = 0
        for c in range(100):
            tmp += arr[r][c]
        if tmp >= mx:
            mx = tmp
    
    # 세로합
    for c in range(100):
        tmp = 0
        for r in range(100):
            tmp += arr[r][c]
        if tmp >= mx:
            mx = tmp
    
    # 대각합
    tmp1 = 0
    tmp2 = 0
    for cross in range(100):
        tmp1 += arr[cross][cross]
        tmp2 += arr[cross][99-cross]
    if tmp1 >= mx:
        mx = tmp1
    if tmp2 >= mx:
        mx = tmp2
    
    print(f"#{test_case}",mx)