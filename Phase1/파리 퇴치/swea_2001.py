import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    M, N = map(int, input().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    sm = 0
    for i in range(M-N+1):
        for j in range(M-N+1):
            tmp = 0
            for k in range(N):
                for l in range(N):
                    tmp += arr[i+k][j+l]
            if tmp > sm : sm = tmp
    print(f"#{test_case}", sm)