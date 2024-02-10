# https://atcoder.jp/contests/abc303/tasks/abc303_b
"""
隣り合ったことがない組合わせは何組あるか
n,m  = 4,2
1 2 3 4
4 3 2 1 
"""


n, m = map(int, input().split())
a = []
for i in range(m):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(m):
    for j in range(n):
        a[i][j] -= 1  # ０始まりなのでそれに合わせる
g = [[False] * n for _ in range(n)]


for i in range(m):
    for j in range(n - 1):  # 調べる組はn-1マスをイメージ
        g[a[i][j]][a[i][j + 1]] = True


ans = 0
# x,y の順番を入れ替えたものは区別しないため y < xの範囲で全探索
for x in range(n):
    for y in range(x):  # x = n-1の範囲
        if g[x][y] or g[y][x]:  # y= x-1の範囲
            continue
        ans += 1

# continue  条件に当てはまったら、その下の処理は実行されずに次のループへ
