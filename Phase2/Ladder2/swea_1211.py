import sys

sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1,T+1):
    input()
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    for lst in arr:
        lst.insert(0,0)
        lst.append(0)

    queue = []

    for i in range(N+1):
        if arr[0][i] == 1:
            queue.append(i)

    result = [0 for _ in range(len(queue))]
    for idx, que in enumerate(queue):
        current = [0,que]
        LR = 0
        while current[0] < N-1:
            if arr[current[0]][current[1]+1] == 1 and arr[current[0]][current[1]-1] == 1: # 횡 이동 상태
                current[1] += LR
                result[idx] += 1
            elif arr[current[0]][current[1]+1] == 1: # 오른쪽 길 있는 경우
                if LR == -1:
                    LR = 0
                    current[0] += 1
                    result[idx] += 1
                    continue
                else:
                    LR = 1
                    current[1] += LR
                    result[idx] += 1
            elif arr[current[0]][current[1]-1] == 1:  # 왼쪽에 길 있는 경우
                if LR == 1: # 왼쪽에 길 있는데 오른쪽으로 이동중이었을 경우
                    LR = 0
                    current[0] += 1
                    result[idx] += 1
                    continue
                else:
                    LR = -1
                    current[1] += LR
                    result[idx] += 1
            else : # 왼쪽 오른쪽 둘 다 길 없는 경우
                current[0] += 1
                result[idx] += 1
    
    
    print(f"#{test_case}",queue[result.index(min(result))]-1)


