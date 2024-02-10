#https://atcoder.jp/contests/abc273/tasks

#フィボナッチ数列の第x項の値を出力する
def f(x, mem):
    if mem[x] != -1:
        return mem[x]
    if x == 0:
        return 0
    if x == 1:
        return 1
    mem[x] = f(x - 2, mem) + f(x - 1, mem)
    return mem[x]

mem = [-1] * 85
print(f(80, mem))

#pythonでのライブラリあり

import math
print(math.factorial(int(input())))
