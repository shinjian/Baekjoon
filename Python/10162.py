# 전자레인지 - https://www.acmicpc.net/problem/10162
t = int(input())
if t % 10 == 0:
    print(t//300, (t%300)//60, (t%60)//10)
else:
    print(-1)