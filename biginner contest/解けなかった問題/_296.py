# https://atcoder.jp/contests/abc296/editorial/6081

array = []
for i in range(8):
    a = list(input())
    array.append(a)

for i in range(8):
    for j in range(8):
        if array[i][j] == "*":
            print(f"{'abcdefgh'[j]}{8-i}")
            exit()
