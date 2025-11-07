import sys
from pprint import pprint

sys.stdin = open('input.txt','r')

T = 10

def bfs(s, connects):
    visited = []
    queue = []
    visited.append(s)
    visited += connects[s]
    queue += connects[s]
    next_queue = queue
    result = [next_queue[:]]
    while next_queue:
        queue = next_queue
        
        next_queue = []
        while queue:
            c = queue.pop(0)
            for next in connects[c]:
                if next not in visited:
                    next_queue.append(next)
        visited += next_queue
        result.append(next_queue[:])
    return max(result[-2])


for test_case in range(1,T+1):
    N, s =list(map(int, input().split()))
    lst = list(map(int,input().split()))
    tmp = list(set(lst))
    connects = {}
    
    for t in tmp:
        connects[t] = []
    
    #print(connects)

    for i in range(len(lst)):
        if i%2 == 1: connects[lst[i-1]].append(lst[i])

    #print(connects)

    print(f'#{test_case}',bfs(s, connects))
