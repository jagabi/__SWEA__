import sys
sys.stdin = open('sample_input.txt','r')

from pprint import pprint

T = int(input())


def bfs(arr):
    si, sj = 0, 0
    ei, ej = len(arr)-1, len(arr)-1
    queue = []
    queue.append([si,sj])
    visited = [[1000000]*len(arr) for _ in range(len(arr))] 
    visited[si][sj] = 0
    while queue: 
        ci, cj = queue.pop(0)
        for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
            ni, nj = ci+di, cj+dj
            if (0 <= ni <= ei) and (0 <= nj <= ej) and (visited[ni][nj] > visited[ci][cj]+1+max(arr[ni][nj]-arr[ci][cj],0)):
                visited[ni][nj] = visited[ci][cj]+1+max(arr[ni][nj]-arr[ci][cj],0)
                queue.append([ni,nj])
    
    return visited[ei][ej]
    



for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    result = bfs(arr)
    print(f'#{test_case}', result)