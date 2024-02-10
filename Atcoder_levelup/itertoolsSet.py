import itertools

# 順列
for seq in itertools.permutations(range(1, 4)):
    print(seq)

# # 重複なしの組み合わせ
# for seq in itertools.combinations(range(1, 10), 3):  # 1~9の範囲で3つ選ぶ
#     print(seq)
# # 配列の中から組み合わせる
# for seq in itertools.combinations(list, 3):  # 配列から3つ選ぶ
#     print(seq)


# # 重複ありの組み合わせ
# for seq in itertools.combinations_with_replacement(range(1, 9), 3):
#     print(seq)
# # 直積
# for seq in itertools.product(range(1, 4), range(1, 4)):
#     print(seq)
