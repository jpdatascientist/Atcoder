# https://atcoder.jp/contests/abc249/tasks/abc249_b
# 与えられる文字が大小の英語を含み、重複した文字がなければOK

# s = Perfect

s = input()
big = False
small = False

for char in s:
    if char.isupper():  # 与えられた文字が大文字かどうか　.islower()小文字
        big = True
    else:
        small = True

diff = len(set(s)) == len(s)  # len(set(s)) 重複せずにカウントできる

if big and small and diff:
    print("Yes")
else:
    print("No")
