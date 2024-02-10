#https://atcoder.jp/contests/abc156/tasks/abc156_b

#整数nをk進数へ変換したときに何桁になるか
n,k = map(int,input().split())
ans = 0
while n < 0:
    n //= k
    ans += 1
print(ans)

