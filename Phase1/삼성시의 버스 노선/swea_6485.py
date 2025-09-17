import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [0]*5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A,B+1):
            arr[i]+=1

    result = []

    P = int(input())

    for _ in range(P):
        j = int(input())
        result.append(arr[j])

    print(f"#{test_case}",*result)


