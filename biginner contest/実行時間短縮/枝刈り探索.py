# https://atcoder.jp/contests/abc214/tasks/abc214_b
"""
a+b+cの総和がS以下である必要があるので、a,b,cは少なくとも0～Sの範囲になっているはずである。
よって、a,b,cを0～Sの範囲でループさせる3重ループを書くので、全部で109通りの組み合わせを確かめていく。
競プロでは組み合わせは多くても107通りくらいしか探索できないので、これでは間に合わない。

breakを使ってループを途中で抜けることにする。
その一定のルールとは「a+b+c≦S」か「abc≦T」のどちらかが満たされなくなったら、即ループを抜けて終了する。
これだけで大幅に探索状態が削減されてTLE（計算時間超過）からACにすることができる。
"""


s, t = map(int, input().split())

a = max(s, t)

count = 0
for i in range(0, s + 1):
    for j in range(0, s + 1):
        for k in range(0, s + 1):
            if i + j + k > s:
                break
            if i * j * k > t:
                break
            count += 1
print(count)
