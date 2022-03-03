# 짝수를 찾아라 - https://www.acmicpc.net/problem/3058
T = int(input())
res = []
for _ in range(T):
    n = list(map(int, input().split()))
    for i in range(7):
        if n[i] % 2 == 0:
            res.append(n[i])
    print(sum(res), min(res))
    res.clear()