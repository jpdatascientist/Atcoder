#https://atcoder.jp/contests/abc331/tasks/abc331_b

"""卵6個入りのパックはS円、卵8個入りのパックはM円、卵12個入りのパックはL円です。
どのパックも何パックでも購入できるとき、
N 個以上の卵を買うために必要な最小の金額を求めてください。
何に対して全探索をしたいのか！！を考える
"""
n,s,m,l = map(int,input().split())

ans = 10**8
for i in range(101):
    for j in range(101):
        for k in range(101):
            #それぞれの卵を買った場合は全検索して、n個以上であれば
            if 6*i + 8*j + 12*k >= n:
                ans = min(ans,s*i + m*j + l*k)
print(ans)