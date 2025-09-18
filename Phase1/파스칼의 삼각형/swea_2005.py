import sys

sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    if N == 1 : print(f"#{test_case}\n1")
    elif N == 2 : print(f"#{test_case}\n1\n1 1")

    else:
        arr = [[1],[1,1]]
        for i in range(1,N-1):
            tmp = [1]
            for j in range(len(arr[i])-1):
                tmp.append(arr[i][j]+arr[i][j+1])

            tmp.append(1)
            arr.append(tmp)


        print(f"#{test_case}")
        for a in arr:
            print(*a)

