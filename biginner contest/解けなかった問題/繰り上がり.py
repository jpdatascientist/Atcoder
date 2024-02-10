# https://atcoder.jp/contests/abc229/editorial/2949

# 非負整数を足した時に繰り上がりが生じるか
a, b = map(int, input().split())

flag = False
"""Aを10で割ったあまりとBを10で割ったあまりの和を求める
   これが10以上であれば繰り上がりが生じる
   これをどちらかが0になるまで続ける
"""

while a > 0 and b > 0:
    if (a % 10) + (b % 10) >= 10:
        flag = True
        break
    a //= 10
    b //= 10
if flag:
    print("Hard")
else:
    print("Easy")
