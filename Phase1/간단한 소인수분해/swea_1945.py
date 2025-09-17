from collections import deque

import sys
sys.stdin = open('input.txt', "r")

T = input()

for t in range(int(T)):
    result = [0,0,0,0,0]
    N = int(input())
    primes = deque([2,3,5,7,11])
    i = 0
    while primes:
        if N % primes[0] == 0:
            N //= primes[0]
            result[i] += 1
        else:
            primes.popleft()
            i += 1

    print(f'#{t+1}', *result)
