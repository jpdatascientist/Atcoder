"""隣り合う2つの要素を比較し、比較した結果によって要素を入れ替える
   左の要素と比較し、左の方が大きければ交換する"""

n = 5
a = [4, 1, 2, 3, 5]


def bubble_sort(a, n):
    # 後ろから２つずつデータを比較し並び替える
    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:  # 左の方が大きければ入れ替え
                a[j - 1], a[j] = a[j], a[j - 1]
        print(*a)
        # return a


bubble_sort(a, n)
