# https://atcoder.jp/contests/abc251/tasks/abc251_b
"""
おもりの中から3つ以下の異なるお守りを選んで、お守りの重さの和がW以下である整数を
良い整数とする。
W 以下の正整数のうち、良い整数は何個ありますか？
"""
# 良い整数は何個あるか？なので、例えば、３・６であれば２つになる
# 良い整数が出た回数ではないことに注意

n, m = 4, 12
s = [3, 3, 3, 3]

flag = [0] * (m + 1)  # 良い整数があった時にそのインデックスの番号を1にして保存する配列　インデックス番号注意

# 異なるおもりから1つ選ぶとき
for i in range(n):
    if s[i] <= m:
        flag[s[i]] = 1

# 異なるおもりから2つ選ぶとき
for i in range(n):
    for j in range(i + 1, n):
        a = s[i] + s[j]
        if a <= m:
            flag[a] = 1

# 異なるおもりから3つ選ぶとき
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = s[i] + s[j] + s[k]
            if a <= m:
                flag[a] = 1
print(sum(flag[1:]))

# 別解
from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

flag = [0] * (W + 1)

# 1つの要素の和をチェック
for s in A:
    if s <= W:
        flag[s] = 1

# 2つの要素の和をチェック
for i, j in combinations(range(N), 2):
    s = A[i] + A[j]
    if s <= W:
        flag[s] = 1

# 3つの要素の和をチェック
for i, j, k in combinations(range(N), 3):
    s = A[i] + A[j] + A[k]
    if s <= W:
        flag[s] = 1

# 答えの計算
ans = sum(flag[1:])
print(ans)
