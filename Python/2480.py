# 주사위 세개 - https://www.acmicpc.net/problem/2480
a, b, c = map(int, input().split())
k = 0
if a == b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
elif a == c:
    print(1000 + ( a * 100))
elif a != b != c:
    max = max(a, b, c)
    print(max * 100)