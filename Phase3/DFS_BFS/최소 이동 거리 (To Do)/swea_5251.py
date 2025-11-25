import sys

sys.stdin = open("sample_input.txt",'r')

T = int(input())


def bfs(lst):
    queue = []
    visited = []
    queue.append(0)

    while queue:
        
    




for test_case in range(1,3):
    N, E = map(int,input().split())
    lst = [[] for _ in range(N+1)]
    
    for _ in range(E):
        s, e, w = map(int,input().split())
        lst[s].append([e, w])
    
    print(lst)

    #print(f'#{test_case}',0) 