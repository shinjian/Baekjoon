# 방학 숙제 - https://www.acmicpc.net/problem/5532
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0:
    result1 = a // c
else:
    result1 = (a//c) + 1

if b % d == 0:
    result2 = b // d
else:
    result2 = (b // d) + 1

print(l - max(result1, result2))