import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    min = 999999
    max = 0

    for i in range(N-M+1):
        if min > sum(arr[i:i+M]):
            min = sum(arr[i:i+M])
        if max < sum(arr[i:i+M]):
            max = sum(arr[i:i+M])


    print(f"#{test_case}",max-min)



