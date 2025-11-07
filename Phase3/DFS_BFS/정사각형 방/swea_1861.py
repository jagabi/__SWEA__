import sys
from pprint import pprint
sys.stdin = open('input.txt','r')

T = int(input())

def bfs(arr,si,sj):
    result = 0
    visited = [[0]*len(arr) for _ in range(len(arr))]
    queue = []
    queue.append([si,sj])
    visited[si][sj] = 1
    while queue:
        if len(queue) > 1: return -1
        ci, cj = queue.pop(0)
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            if (ci+di < N and cj+dj < N) and ((arr[ci+di][cj+dj] == arr[ci][cj] + 1) or (arr[ci+di][cj+dj] == arr[ci][cj] - 1)):
                if visited[ci+di][cj+dj] == 0:
                    queue.append([ci+di,cj+dj])
                    visited[ci+di][cj+dj] = visited[ci][cj]+1

    for visit in visited:
        if max(visit) > result: result = max(visit) 

    #print(result)
    return result


for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    #pprint(arr)
    #print()

    result = []
    for i in range(N):
        for j in range(N):
            result.append([arr[i][j],bfs(arr,i,j)])

    result.sort(key = lambda x: x[0])
    result.sort(key = lambda x: x[1],reverse=True)

    print(f'#{test_case}', result[0][0], result[0][1])