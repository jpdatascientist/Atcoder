# ルートの計算　√（（x１ーx２）**2＋（y１ーy２）**２）

n = int(input())
x = []
y = []

for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

import math

ans = 0

# 二重ループ　全ての組み合わせの列挙！
for i in range(n):
    for j in range(i + 1, n):
        length = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        ans = max(ans, length)
print(ans)
