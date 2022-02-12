# 제로 - https://www.acmicpc.net/problem/10773
k = int(input())
list = []
for i in range(k):
    n = int(input())
    if n == 0:
        list.pop()
    else:
        list.append(n)
print(sum(list))