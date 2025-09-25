import sys

sys.stdin = open('sample_input.txt', 'r')

T = 10


def landscape(arr,j,i):
    if arr[j][i-1] == 1:
        return False
    if arr[j][i-2] == 1:
        return False
    if arr[j][i+1] == 1:
        return False
    if arr[j][i+2] == 1:
        return False
    return True

for tast_case in range(1, 2):
    N = int(input())
    towers = list(map(int,input().split()))

    result = 0
    arr = [[0]*(N+4) for i in range(256)]

    for i in range(N):
        for j in range(towers[i]):
            arr[j][i+2] = 1

    print(arr)


    #arr[층][건물]

    for j in range(2,len(arr[0])-1):
        for i in range(len(arr)):
            if landscape(arr,j,i): result+=1

    print(result)
