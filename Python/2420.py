# 사파리월드 - https://www.acmicpc.net/problem/2420
n, m = map(int, input().split())
if n > m:
    print(n - m)
else:
    print(m - n)