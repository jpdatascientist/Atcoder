# https://atcoder.jp/contests/abc181/tasks/abc181_b

"""1以上x以下の整数の和 x*(x+1) //2
a以上b以下の整数の和 b*(b+1) - a*(a-1)
"""

n = int(input())

total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += ((b * (b + 1)) // 2) - ((a * (a - 1)) // 2)

print(total)
