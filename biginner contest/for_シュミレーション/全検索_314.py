"""
n人の人は(1〜n番目)それぞれci個の配列を持っている
その配列の中に対象の数字があればその人数と番号を昇順に出力する
"""
#配列の習得・minの使用方法

n = int(input())
A = []
B = []
for i in range(n):
    A.append(int(input()))
    B.append(list(map(int,input().split())))
x = int(input())

vec = []#i番目の人を入れる　今はインデックス番号
for i in range(n):
    for j in range(len(B[i])):
        if B[i][j] == x:
            vec.append(i)

min_vec = 37  #問題より個数の最大値は３７
for i in vec:
    min_vec = min(A[i],min_vec)#対象の数字を持っているi番目の人の個数の最小値を見つける

ans = []
for i in vec:
    if A[i] == min_vec:
        ans.append(i+1)

print(len(ans))
print(*ans)#もしansに何も入っていない場合は何も出力されない



