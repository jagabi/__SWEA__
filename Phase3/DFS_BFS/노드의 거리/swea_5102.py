import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    links = []
    for _ in range(E):
        link = list(map(int, input().split()))
        links.append([link[0],link[1]])
    
    S, G = list(map(int, input().split()))

    
    node = [set() for i in range(V+1)]

    for link in links:
        node[link[0]].add(link[1])
        node[link[1]].add(link[0])
    

    leaves = []
    visited = []

    leaves.append(S)
    visited.append(S)
    cnt = 0
    result = 0
    while leaves:
        tmp = []
        for leaf in leaves:
            for n in node[leaf]:
                if n not in visited:
                    visited.append(n)
                    tmp.append(n)
        cnt +=1
        leaves = tmp
        if G in leaves: 
            result = cnt
            break
    
    print(f"#{test_case}",result) 