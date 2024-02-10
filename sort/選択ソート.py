"""選択ソート（昇順）
①未整列のデータの中から一番小さい要素を選択する
②選択した要素と未整列のデータの先頭を入れ替える"""

n = 5
a = [4, 1, 3, 5, 2]


"""探索範囲の最小値を発見し、iの位置に置くこと"""


def selection_sort(a, n):
    for i in range(0, n - 1):
        min_index = i  # 入れ替え対象をセット 未整列の先頭の位置を仮に最小値とする
        for j in range(i + 1, n):  # 次のインデックス以降の要素を順に見ていく
            if a[j] < a[min_index]:  # セットした値よりも小さな値があれば
                min_index = j  # その位置を最小値として上書き
                #print(min_index)

        a[i], a[min_index] = a[min_index], a[i]

    return a


print(selection_sort(a, n))

