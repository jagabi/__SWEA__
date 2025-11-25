import sys

sys.stdin = open('input.txt','r')

T = int(input())

INF = 10000000

def bfs(arr,si,sj,ei,ej):
    queue = []
    visited = [[INF]*(ei+1) for _ in range(ei+1)]
    queue.append([si,sj])
    visited[si][sj] = 0
    while queue:
        ci,cj = queue.pop(0)        
        for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
            ni, nj = ci+di, cj+dj
            if (0 <= ni <= ei) and (0 <= nj <= ej) and (visited[ni][nj] > visited[ci][cj] + arr[ni][nj]):
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                queue.append([ni,nj])

    return visited[ei][ej]




for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        tmp = []
        for c in str(input()):tmp.append(int(c))
        arr.append(tmp)
    print(f'#{test_case}', bfs(arr,0,0,N-1,N-1))
