import sys

sys.stdin = open("sample_input.txt", 'r')

from collections import deque


T = int(input())

def bfs(s, e):
    queue = deque()
    visited = [0] * 1000001
    queue.append(s)
    visited[s] = 1

    while queue:
        current = queue.popleft()
        if current == e:
            return visited[current] -1

        for i in ((current+1),(current-1),(current*2),(current-10)):
            if 1 <= i <= 1000000 and visited[i] ==0:
                queue.append(i)
                visited[i] = visited[current]+1

    return -1

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    print(f"#{test_case}",bfs(N, M))
    