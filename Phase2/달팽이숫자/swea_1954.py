import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    if N == 1 : 
        print(f"#{test_case}\n",1,sep="")
        continue
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]

    lst = []
    
    
    for i in reversed(range(1, N)):
        lst.append(i)
        lst.append(i)
    lst = deque(lst)
    #print(lst)
    arr = [[i for i in range(1,N+1)]]
    for _ in range(N-1): arr.append([0]*N)

    #print(*arr,sep="\n")
    k = 0
    cnt = N+1
    current = [0,N-1]

    while lst:
        q = lst.popleft()
        for _ in range(q):
            current[0] += dr[k%4]
            current[1] += dc[k%4]
            arr[current[0]][current[1]] = cnt
            cnt += 1
        k += 1

    print(f"#{test_case}")
    for nums in arr:
        print(*nums)
        


    





'''
1,2,3,4,5
16,17,18,19,6
15,24,25,20,7
14,23,22,21,8
13,12,11,10,9



6 5 5 4 4 3 3 2 2 1 1

5 4 4 3 3 2 2 1 1
'''