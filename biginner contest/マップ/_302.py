#https://atcoder.jp/contests/abc302/tasks/abc302_b
h,w = map(int,input().split())
S = [input() for _ in range(h)]
T = "snuke"

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for si in range(h):
    for sj in range(w):
        for v in range(8):#この５文字を試す前に８方向を試したいので
            i, j = si, sj
            for k in range(5):
                if i < 0 or j < 0 or i >= h or j >= w:
                    break
                if S[i][j] != T[k]:
                    break

                if k == 4:#もしbreakせずに回り切ったら
                    i, j = si, sj
                    for nk in range(5):#答えを出力するためのループ
                        print(i + 1, j + 1)
                        i += di[v]
                        j += dj[v]
                    exit()#答えを出力したら終了
                #上記のコードは右矢印横方向のみであるので、８方向へ試したい
                i += di[v]
                j += dj[v]