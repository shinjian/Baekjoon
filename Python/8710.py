# Koszykarz - https://www.acmicpc.net/problem/8710
k, w, m = map(int, input().split())
sum = w - k
if sum % m != 0:
    sum = (sum//m) + 1
print(sum)