#https://atcoder.jp/contests/abc304/tasks/abc304_a
"""
ある特定の位置からインデックス番号順に出力する
(p+i)modN 特定の位置=p N=全体個数

"""
n = int(input())
s = []
a = []
for _ in range(n):
    s_i, a_i = input().split()
    s.append(s_i)
    a.append(int(a_i))

si = 0  # 一番小さいインデックス番号を探す
for i in range(n):
    if a[i] < a[si]:
        si = i#ループが回り切ったら、si＝最小のインデックス

#起点のインデックスから順に出力
for i in range(n):
    ni = (si + i) % n
    print(s[ni])
