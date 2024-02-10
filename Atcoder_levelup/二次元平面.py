"""
2点を通る直線の公式
(y-y1)(x2-x1)= (y2-y1)(x-x1)
３点を通る直線の公式
(y3-y1)(x2-x1) = (y2-y1)(x3-x1)
"""

# 0~4の5種類から3つの組み合わせをどう作成するか？　三重ループについて
# 内側のループが回りきらなくなったら、その上のループが開始される
a = 5
for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a):  # i=3 j=4となった場合k=5でkには何も入らず処理なし
            print(i, j, k)

# n = int(input())
# point = [[int(x) for x in input().split()] for i in range(n)]

# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             x1, y1 = point[i][0], point[i][1]
#             x2, y2 = point[j][0], point[j][1]
#             x3, y3 = point[k][0], point[k][1]

#             if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
#                 print("Yes")
#                 exit()

# print("No")
