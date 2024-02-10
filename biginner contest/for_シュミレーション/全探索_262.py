"""
N 頂点  M 辺の単純無向グラフが与えられます。頂点には 1,…,N の番号が付けられており、
i(1≤i≤M) 番目の辺は頂点 Uiと頂点 Viを結んでいます。
以下の条件を全て満たす整数 
a,b,c の組の総数を求めてください。
"""


n,m = map(int,input().split())
adj = [[False] * n for i in range(n)]

for i in range(m):
    u,v = map(int,input().split())
    #インデックスは0スタートなので、入力を合わせる
    u -= 1
    v -= 1
    adj[u][v] = True
    adj[v][u] = True

ans = 0
for i in range(n):
    for j in range(i + 1,n):
        for k in range(j + 1,n):
            if adj[i][j] and adj[j][k] and adj[k][i]:
                ans += 1
print(ans)


