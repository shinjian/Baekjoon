# 소수 찾기 - https://www.acmicpc.net/problem/1978
n = int(input())
num = list(map(int, input().split()))
count = 0
for i in num:
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        count += 1
print(count)