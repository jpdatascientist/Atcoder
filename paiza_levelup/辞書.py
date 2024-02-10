# # 2
# # MIDORIKAWA
# # KIRISHIMA
# # 2
# # KIRISIHMA 1
# # KIRISHIMA 2
# # それぞれの値を合計して、名前のアルファベット順に値を出力する
# n = int(input())
# name_array = {}
# for i in range(n):
#     a = input()
#     name_array[a] = 0  # 初期値０の辞書を作成
#
# m = int(input())
# for i in range(m):
#     p, q = input().split()
#     q = int(q)
#     name_array[p] += q  # 辞書の名前：キーに対して値を代入して更新
# name_array2 = sorted(
#     name_array.items()
# )  # 辞書をキーでソート　　name_array2 = list(name_array.keys()) キーをリストにする　name_array2 = sort() キーだけソートするやり方も
# for i in name_array2:
#     print(i[1])
#
# # 　問題で、最後に名前が与えられた際にその値を出力する
# n = int(input())
# dmg = {}
# for i in range(n):
#     s = input()
#     dmg[s] = 0
# m = int(input())
# for i in range(m):
#     [p, a] = input().split()
#     a = int(a)
#     dmg[p] += a
# S = input()
# print(dmg[S])
a = input()
