# https://atcoder.jp/contests/abc264/tasks/abc264_b

"""
グリッドが中央のマス（ 8 行目 8 列目のマス）を中心として対称で規則的な形をしていることを利用すると、
与えられたグリッドでは、中央のマスからの”距離”が奇数のマスは黒、偶数のマスは白になっています。 
具体的には、
R 行目 C 列目のマスが黒色であるのは、そのマスと中央のマスからのチェビシェフ距離（チェス盤距離）
max(abs(r-8),abs(c-8)) 
が奇数の時に黒色になる
"""

r, c = map(int, input().split())

if (max(abs(r - 8), abs(c - 8))) % 2 != 0:
    print("black")
else:
    print("white")
