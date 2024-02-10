# n=314 k=2  nに対してk回fを行う
n, k = map(int, input().split())


def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)
    return int(x)


def g2(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = "".join(x)
    return int(x)


def f(x):
    return g1(x) - g2(x)


a = n  # 初期値をaに代入する
for i in range(k):  # f(a)をk回行う
    a = f(a)  # 取り出されたaをまた再代入してf(a)を行う

print(a)
