import sys


sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    tmp = list(map(int,input().split()))
    gas_station = [False for i in range(N+1)]
    for t in tmp: gas_station[t] = True
    gas_station[len(gas_station)-1] = True
    for _ in range(K): gas_station.append(False)
    #print(gas_station)

    result = 0
    current = 0

    # 충전할 수 있는 곳 멀리서부터 서치
    while current < N:
        tmp = current
        for i in reversed(range(current+1,current+K+1)):
            if gas_station[i]:
                current = i
                result += 1
                break
        if tmp == current:
            result = 1
            break
    print(f"#{test_case}", result-1)
