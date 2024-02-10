# https://atcoder.jp/contests/abc147/tasks/abc147_b
# 与えられる文字が回文になるために文字を変える場合、何回の変える作業が必要か

s = list(input())

count = 0
length = len(s)
for i in range(length // 2):
    if s[i] != s[length - 1 - i]:
        count += 1
print(count)
