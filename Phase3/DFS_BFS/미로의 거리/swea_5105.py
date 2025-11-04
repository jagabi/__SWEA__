import sys
from pprint import pprint

sys.stdin = open("sample_input.txt", "r")

T = int(input())


def bfs(si, sj, ei, ej, arr):
    visited = [[0]*(len(arr)+2) for _ in range(len(arr)+2)]
    queue = []
    queue.append([si,sj])

    #print(visited)
    while queue:
        ci, cj = queue.pop(0)
        if ci == ei and cj == ej:
            return visited[ci][cj]-1
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            ni, nj = ci+di, cj+dj
            if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append([ni,nj])
                visited[ni][nj] = visited[ci][cj]+1

    return 0


for test_case in range(1, T+1):
    N = int(input())
    arr = [[1 for _ in range(N+2)] for __ in range(N+2)] 
    si, sj = 0, 0
    ei, ej = 0, 0

    for i in range(N):
        tmp = ['1'] + list(map(str,input())) + ['1']
        for j in range(N+2):
            arr[i+1][j] = int(tmp[j])
            if int(tmp[j]) == 2: 
                si, sj = i+1, j
            elif int(tmp[j]) == 3:
                ei, ej = i+1, j

    result = bfs(si,sj,ei,ej,arr)

    #pprint(arr)
    #print(si,sj)
    #print(ei,ej)

    print(f"#{test_case}",result)








