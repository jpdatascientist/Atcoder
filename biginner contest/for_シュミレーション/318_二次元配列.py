# https://atcoder.jp/contests/abc318/submissions/me
#シートを塗りつぶすというよりかは、マスを用意して、その範囲にある座標を塗りつぶすという解法

n = int(input())
#二次元配列の作成
g = [[False for i in range(100)] for j in range(100)]
# g = [[false] * 100 for i in range(100)]

for k in range(n):
    a,b,c,d = map(int,input().split())
    #a~b-1までの範囲を塗りつぶす
    for i in range(a,b):
        #c~d-1までの範囲を塗りつぶす
        for j in range(c,d):
            g[i][j] = True

ans = 0
for i in range(100):
    for j in range(100):
        if g[i][j] == True:
            ans += 1


