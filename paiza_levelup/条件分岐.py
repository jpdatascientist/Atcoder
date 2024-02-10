# 全ての条件が当てはまらない時の制御構文
c = [input() for i in range(a)]
found = False
for i in c:
    if b in i:
        found = True
        print(i)

if not found:
    print("None")


# 整数 N, M が与えられます。
# N が何回 M で割れるかを求め、出力してください
# 入力例：81 3  出力例：4
N, M = map(int, input().split())

div_count = 0
while True:
    if N % M == 0:
        N //= M #左辺の値を右辺の整数のみで徐して左辺へ代入
        div_count += 1#割った回数をカウント
    else:
        break  #N が M で割れなくなった場合に breakすることで無限ループからブレイクする

print(div_count)
