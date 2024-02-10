"""グリッドの行数 H と列数 W が与えられるので、マス (y,x) から次の移動を 
1 回おこなった時に到達することができるマスを '*' , それ以外のマスを '.' にしたグリッドを出力してください。
現在いるマスを (y,x) としたとき、(y+1,x), (y-1,x), (y,x+1), (y,x-1) のいずれかのマスに移動する。
ただし、グリッドの外へは移動することができません。前後左右へ移動する
なお、グリッドの左上・右上・左下・右下のマスをそれぞれ (0,0), (0,W-1), (H-1,0), (H-1,W-1) とします。
到達できるマスに (y,x) が含まれることに気をつけてください。"""

h, w = 3, 3
y, x = 1, 1


# 枠外に出力するこtはできないのでif文を使って制御
def exchange_map(y, x):
    for i in range(h):
        grid = ""
        for j in range(w):
            able_to_reach = False
            if i == y:
                if 0 <= j and j == x - 1:
                    able_to_reach = True
                if j < w and j == x + 1:
                    able_to_reach = True
            if j == x:
                if 0 <= i and i == y - 1:
                    able_to_reach = True
                if i < h and i == y + 1:
                    able_to_reach = True
            if i == y and j == x:
                able_to_reach = True
            if able_to_reach:
                grid += "*"
            else:
                grid += "."
        print(grid)


exchange_map(y, x)

# 幅優先探索
# 現在いるマスから1回移動した先の頂点を訪問する操作を未訪問の頂点が無くなる、もしくは移動できなくなるまで繰り返す探索

"""グリッドの行数 H と列数 W が与えられるので、マス (y,x) から次の操作を 1 回としたとき、 
3 回以内に到達することができるマスを '*' , それ以外のマスを '.' にしたグリッドを出力してください。"""
