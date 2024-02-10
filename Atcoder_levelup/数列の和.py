N = int(input())
A = list(map(int,input().split()))

mod = 10 ** 9 + 7

# 1,2,3,4 の数列の和をmodで割ったあまりを加算していく

a_num = sum(A)
ans = 0
for i in range(N):
    a_num -= A[i]
    ans += A[i] * a_num
    ans %= mod

print(ans)


