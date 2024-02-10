"""
このPythonコードは、入力としてnとリストaを受け取り、
リスト内に0が含まれているかどうかを判定します。
リストaの各要素をループでチェックし、要素が0の場合、
res をTrueに設定（フラグを立て）します。最終的に、res の値に応じて、
"Yes" または "No" を出力します。
"""
#フラグ管理の原則は条件を満たすものがある場合にTrueとなること

n = int(input())
a = list(map(int, input().split()))

res = False  # 初期値は False

for num in a:
    if num == 0:
        res = True  # 0 だったら True (フラグを立てる)

if res:
    print("Yes")
else:
    print("No")

"""条件が見つかったかどうかだけでなく、どこにあったかを知りたい時"""

n = int(input())
a = list(map(int, input().split()))

findID = -1  # ここに見つかった場所を格納します (実はこれ自体がフラグの役割を果たします)

for i in range(n):
    if a[i] == 0:  # 見つかったら、
        findID = i  # 場所を記録して、
        break       # break

if findID != -1:
    print(findID)# インデックス番号注意
else:
    print("No")

"""条件のものを全て拾いたい時"""
n = int(input())
a = list(map(int, input().split()))

findIDs = []  # 0 の場所を格納するリスト

for i in range(n):
    if a[i] == 0:  # 見つかったら、
        findIDs.append(i)  # 場所を記録して、今度は break しない！！！ (すべて求めたいため)

# 結果出力
print("nums of zeros:", len(findIDs))  # 何個あったか
for idx in findIDs:
    print(idx, "th")


"""出現回数をカウントしたい時"""

n = int(input())
a = list(map(int, input().split()))

res = 0  # 初期値は 0

for num in a:
    if num == 0:
        res += 1  # 0 だったらカウントする

print(res)
