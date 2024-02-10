# https://atcoder.jp/contests/abc274/tasks/abc274_b

"""
二次元配列をとって、その列を見る
列の中に”＃”が含まれている場合カウントし、列のなかで何個それがあるか出力する
"""
h, w = map(int, input().split())

ar = [list(input()) for _ in range(h)]

ans = []
for j in range(w):
    count = 0  # 列の中で何回現れるか
    for i in range(h):
        if ar[i][j] == "#":
            count += 1
    ans.append(count)
print(*ans)
