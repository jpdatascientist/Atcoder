# 順列を列挙してくれるライブラリ itertools
import itertools

a = 4  # 1からn-1までの順列
for root in itertools.permutations(range(1, a)):
    print(root)

# 作った順列と対応する経路の移動時間を計算し、対象の数字となるものを数えて出力する

n, k = map(int, input().split())
time = []
for i in range(n):
    T = list(map(int, input().split()))
    time.append(T)

# 0~n-1の順列~0というルートを全て確認する
ans = 0  # 合計がkとなったルートを保存する変数
for root in itertools.permutations(range(1, n)):  # 最初の経路の組み合わせ
    now_time = 0
    now_time += time[0][root[0]]

    now_city = root[0]
# 作成した順列と対応する経路の移動時間を計算し、Kとなるモノを数えて出力すれば良い
    for i in range(1, n - 1):  # len(root) -1
        to_city = root[i]
        now_time += time[now_city][to_city]
        now_city = to_city

    now_time += time[now_city][0]  # 最後に訪れたところから都市１へ戻る
    if now_time == k:
        ans += 1

print(ans)
