import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')

def bfs(arr,si,sj):
    queue = []
    visited = []
    queue.append([si,sj])
    visited.append([si,sj])
    
    while queue:
        ci, cj = queue.pop(0)
        if arr[ci][cj] == 3:
            return 1
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            if arr[ci+di][cj+dj] != 1 and [ci+di,cj+dj] not in visited:
                queue.append([ci+di,cj+dj])
                visited.append([ci+di,cj+dj])
    return 0

for test_case in range(1,11):
    input()
    arr = []

    si, sj = -1, -1

    for _ in range(16):
        arr.append(list(map(int, input())))

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                si, sj = i, j

    #pprint(arr)   
    #print(si,sj)

    print(f'#{test_case}',bfs(arr, si, sj))



