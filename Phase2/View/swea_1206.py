import sys

sys.stdin = open('sample_input.txt', 'r')

T = 10


def check(arr,i,j):
    if arr[i][j-1] == 1:
        return False
    if arr[i][j-2] == 1:
        return False
    if arr[i][j+1] == 1:
        return False
    if arr[i][j+2] == 1:
        return False
    return True

for test_case in range(1, T+1):
    N = int(input())
    towers = list(map(int,input().split()))

    result = 0
    arr = [[0 for _ in range(N)] for __ in range(256)]

    

    for idx, height in enumerate(towers):
        for h in range(height):
            arr[h][idx] = 1

    for c in reversed(range(2, len(arr[0])-1)):
        for r in reversed(range(len(arr))):
            if arr[r][c] == 1:
                if check(arr,r,c):
                    result += 1
                else:
                    break

    print(f"#{test_case}",result)
