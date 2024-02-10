# 入力
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 横方向
for i in range(H):
    for j in range(W-4):#w回したらオーバーしてしまうので、６−４リストの文字数-探す文字数分-1
                        #一つの座標が決まって、その残りの文字数分だけ増やすようにする
        # 左から右に"snuke"なら座標を出力
        if S[i][j] == "s" and S[i][j+1] == "n" and S[i][j+2] == "u" and S[i][j+3] == "k" and S[i][j+4] == "e":
            for k in range(5):#探す文字数分
                print(i+1, j+1+k) #一つづつ４文字まで増やして表示させたいから
        # 右から左に"snuke"なら座標を出力
        elif S[i][j] == "e" and S[i][j+1] == "k" and S[i][j+2] == "u" and S[i][j+3] == "n" and S[i][j+4] == "s":
            for k in range(5):
                print(i+1, j+1+4-k)#"s"の座標から一つづつ減らして表示させたいから
# 縦方向
for i in range(H-4):
    for j in range(W):
        # 上から下に"snuke"なら座標を出力
        if S[i][j] == "s" and S[i+1][j] == "n" and S[i+2][j] == "u" and S[i+3][j] == "k" and S[i+4][j] == "e":
            for k in range(5):
                print(i+1+k, j+1)
        # 下から上に"snuke"なら座標を出力
        elif S[i][j] == "e" and S[i+1][j] == "k" and S[i+2][j] == "u" and S[i+3][j] == "n" and S[i+4][j] == "s":
            for k in range(5):
                print(i+1+4-k, j+1)
# 右下がり方向
for i in range(H-4):
    for j in range(W-4):
        # 左上から右下に"snuke"なら座標を出力
        if S[i][j] == "s" and S[i+1][j+1] == "n" and S[i+2][j+2] == "u" and S[i+3][j+3] == "k" and S[i+4][j+4] == "e":
            for k in range(5):
                print(i+1+k, j+1+k)
        # 左下から右上に"snuke"なら座標を出力
        elif S[i][j] == "e" and S[i+1][j+1] == "k" and S[i+2][j+2] == "u" and S[i+3][j+3] == "n" and S[i+4][j+4] == "s":
            for k in range(5):
                print(i+1+4-k, j+1+4-k)
# 右上がり方向
for i in range(H-4):
    for j in range(4,W):
        # 右上から左下に"snuke"なら座標を出力
        if S[i][j] == "s" and S[i+1][j-1] == "n" and S[i+2][j-2] == "u" and S[i+3][j-3] == "k" and S[i+4][j-4] == "e":
            for k in range(5):
                print(i+1+k, j+1-k)
        # 右下から左上に"snuke"なら座標を出力
        elif S[i][j] == "e" and S[i+1][j-1] == "k" and S[i+2][j-2] == "u" and S[i+3][j-3] == "n" and S[i+4][j-4] == "s":
            # print(i,j)
            for k in range(5):
                print(i+1+4-k, j+1-4+k)
