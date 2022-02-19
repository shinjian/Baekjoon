# 뒤집힌 덧셈 - https://www.acmicpc.net/problem/1357
def res(n):
    res = ''
    for i in range(len(n), 0, -1):
        res += n[i-1]
    return res.lstrip('0')
x, y = map(str, input().split())
print(res(str(int(res(x)) + int(res(y)))))