# (X,Y)のマスから上、下、右、左方向へ、壁に当たるまで何マス進めるか調べればよい。
# (1)与えられた文字列を二次元配列として受け取る
# (2)マス(X,Y)から上、下、右、左方向へ壁に当たるまで進み、それぞれの方向について見えるマス(=壁に当たるまでに通ったマス)の個数をカウントする
# (3)マス(X,Y)自身の分を見えるマスのカウントに足す(+1)
# (4)見えるマスのカウント数を出力する

H, W, X, Y = 4, 4, 2, 2
"""##..
   ...#
   #.#.
  .#.#"""

H, W, X, Y = map(int, input().split())

grid = []
for i in range(H):
    S = input()
    S = list(S)  # ここでlistにしないと一個一個の分割とならない
    grid.append(S)


X -= 1  # インデックス番号と合わせる
Y -= 1

ans = 0  # マス（X,Y）から上下左右に壁に当たるまで進み（壁に当たるまで通ったマスをカウント）
# 上
for i in range(1, H):
    if 0 <= X - i < H:
        if grid[X - i][Y] == "#":
            break
        else:
            ans += 1
# 下
for i in range(1, H):
    if 0 <= X + i < H:
        if grid[X + i][Y] == "#":
            break
        else:
            ans += 1
# 左
for i in range(1, W):
    if 0 <= Y - i < W:
        if grid[X][Y - i] == "#":
            break
        else:
            ans += 1
# 右
for i in range(1, W):
    if 0 <= Y + i < W:
        if grid[X][Y + i] == "#":
            break
        else:
            ans += 1

ans += 1

print(ans)
