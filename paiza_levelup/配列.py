# 内包表記を使って二次元配列を作成する
a = [[0 for j in range(3)] for i in range(2)]
print(a)
# [[0, 0, 0], [0, 0, 0]]
a[0][0] = 1
print(a)
# [[1, 0, 0], [0, 0, 0]]

# forを使って二次元配列を作成
# a = [[1,2,3,4],[5,6,7,8]]
for i in range(len(a)):
    for j in range(a[i]):
        print(a[i][j])
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# 配列を表示する 横並びで
a = 2
b = 3
c = [[3 ,4 ,5],[7 ,8 ,9]]
#3 4 5
#7 8 9と表示するためには
for i in range(a):
    for j in range(b):
        if j != b - 1:
            print(c[i][j], end = " ")
        else:
            print(c[i][j])

# 二次元配列をint型に直す
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])
print(arr)
# [[1, 2], [3, 4], [5, 6]]
arr = [[int(x) for x in y] for y in arr]
print(arr)
# [[1, 2], [3, 4], [5, 6]]

# 二次元配列
for i in range(1,10): #これは段の数
    for j in range(1,10) # i段目の要素の数

# 二次元配列の各要素の最大値を出力する
n = 10 #Aの配列の要素数
k = 11 #Bの配列の要素数
A = [1,2,3,4,5,6,7,8,9,10]
B = [98,90,111,4,7,9,23,67,9,13,55]

ans = 0
for i in range(n):
    for j in range(k):   #配列の要素数が合ってればoutofrangeになることはない
        multi = A[i] * B[j]
        if multi > ans:
            ans = multi
print(ans)

#転置行列を作成
# N行K列の配列をK行N列の配列にする
array = [[1,2],[4,5],[7,8]] 
for i in range(len(array[i])):
    for j in range(len(array)):
        if j == len(array) - 1:
            print(array[j][i])
        else:
            print(array[j][i],end=" ")
# 1,4,7
# 2,5,8

# 三角形の探索　直角三角形であるかの判定
# 三角形が直角三角形であるかどうかを三重ループで調べることができます。
# しかし、N^3 では実行時間制限に間に合わなくなってしまいます。
# そこで、 a + b + c = N という条件を利用します。
# a , b の値が決まったとき、c の値は c = N - a - b で求めることができます。
n = int(input())#三辺の和

flag = False
for b in range(1, n):
    for c in range(1, n - b):
        a = n - b - c
        if a ** 2 == b ** 2 + c ** 2:
            flag = True

if flag:
    print("YES")
else:
    print("NO")
