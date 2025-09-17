import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())




for t in range(1,T+1):
    N, Q = map(int, input().split())
    result = [0]*N
    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for k in range(L-1,R):
            result[k]=i

    print(f"#{t}",*result)

