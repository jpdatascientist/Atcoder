"""
三角形が作れるか、1≤i<j<k≤N の組であって次の 2 つの条件の両方を満たすものの個数
三辺の長さすべて異なる
三角形が存在する = i + j < k

"""
# n=5 list [4,4,9,7,5]

n = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # こちらの書き方の方がスッキリ 同じだったら、処理せず次ループ
            if A[i] == A[j]:
                continue
            if A[j] == A[k]:
                continue
            if A[k] == A[i]:
                continue
            # i< j < kを満たす条件コツ
            if A[i] + A[j] + A[k] <= (max(A[i], A[j], A[k])) * 2:
                continue
            # 上記に合致しなければ
            ans += 1

ruse
"""
vec リストを昇順にソートします。
外側のループ i は、vec リストの要素を順番に見ていきます。
i が 0 から n - 1 まで動きます。
中間のループ j は、i より前の位置の要素を見ていきます。
つまり、i の左側にある要素を順番に選びます。
これによって、vec[i] より小さい要素を選びます。j が 0 から i - 1 まで動きます。
内側のループ k は、j より前の位置の要素を見ていきます。
つまり、i や j の左側にある要素を順番に選びます。
これによって、vec[i] や vec[j] より小さい要素を選びます。k が 0 から j - 1 まで動きます。
"""
n = 7
vec = [2, 3, 5, 6, 8, 9, 7]
vec.sort()


# i=3から出ないとループが回せなくなる
for i in range(n):
    for j in range(i):
        for k in range(j):
            print(i, j, k)


"""３つ選んで三角形が作成できる場合は、個数をできない場合は０を出力
三角形の作成条件
a+b>c
b+c>a
c+a>b

"""
N = int(input())
vec = list(map(int, input().split()))
# ここでソートすることで、iがj,kより必ず大きいことがわかるので
# vec[j] + vec[k] > vec[i]のみチェックすれば良いことがわかる
vec.sort()

ans = 0

for i in range(N):
    for j in range(i):
        for k in range(j):
            if vec[k] != vec[j] and vec[i] != vec[j] and vec[k] + vec[j] > vec[i]:
                ans += 1

print(ans)
