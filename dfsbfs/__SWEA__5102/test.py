import sys
sys.stdin = open("input.txt","r")


def bfs(s,e):
    queue = []
    visited = [0]*(V+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        current = queue.pop(0)
        if current == e:
            return visited[e]-1
        for node in arr[current]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = visited[current]+1
            else:
                continue
    return 0
T= int(input())

for test_case in range(1,T+1):
    V, E = map(int, input().split())
    
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        arr[s].append(e)
        arr[e].append(s)
    target_s, target_b = map(int,input().split())

    #print(arr)
    #print(bfs(1,6))
    print(f"#{test_case} {bfs(target_s,target_b)}")

            
        