import sys

sys.stdin = open('input.txt','r')

T = 10

for test_case in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    while N > 0 :
        mx = max(boxes)
        mn = min(boxes)
        boxes[boxes.index(mx)]-=1
        boxes[boxes.index(mn)]+=1
        N-=1

    print(f'#{test_case} {max(boxes)-min(boxes)}')