"""挿入ソートの改良版"""
n = 10
a = [7, 6, 10, 2, 5, 4, 8, 3, 9, 1]
h = [4, 1]


def insertion_sort(a, n, h):
    """アルゴリズムが正しく実装されていることを確認するために導入するカウンタ変数、
    ソート処理には関係がないことに注意"""
    num_of_move = 0

    for i in range(h, n):
        x = a[i]
        j = i - h

        while j >= 0 and a[j] > x:
            a[j + h] = a[j]
            j -= h
            num_of_move += 1

        a[j + h] = x

    print(num_of_move)
    print(*a)


def shell_sort(a, n, h):
    for h_i in h:
        insertion_sort(a, n, h_i)


# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())
# h = list(map(int, input().split()))

shell_sort(a, n, h)
