s, k = input().split()

k = int(k)

Sset = set()  # リストだと重複するものも入ってしまうため
import itertools

for i in itertools.permutations(range(len(s))):  # 0~2までの組み合わせ
    # 作成した文字を記録する変数
    Sword = ""
    for j in i:
        Sword += s[j]
    # 作成した文字をSsetへ追加　addであることに注意
    Sset.add(Sword)

# print(Sset)
# setのままだとソートできないのでリストへ変換
Sset = list(Sset)
Sset.sort()
print(Sset[k - 1])


# セットの作成：変数名=set()
# セットへ要素の追加：変数名.add(要素)
# Xset.add("aaa")
# Xset.add("bbb")
# 重複した要素を追加しようとしても無視される
# Xset.add("aaa")
