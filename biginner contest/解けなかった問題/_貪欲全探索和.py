# https://atcoder.jp/contests/abc167/tasks/abc167_b
# １をできるだけたくさん取って、取れなくなったら０をとって・・・
# 全探索をするとTEL

a, b, c, k = map(int, input().split())
xa = min(a, k)  # aの枚数を取れるだけとる
k -= xa
xb = min(b, k)  # bの枚数を取れるだけとる
k -= xb
xc = k  # 残りの枚数

print(xa * 1 + xb * 0 + xc * -1)

print(a)