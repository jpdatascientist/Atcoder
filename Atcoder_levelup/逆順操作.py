# ボールが奇数の場合と偶数の場合によって、場合分け、nが０になるまで行う

n = int(input())
ans = ""

while n > 0:
    if n % 2 == 0:
        ans = "B" + ans
        n //= 2
    else:
        ans = "A" + ans
        n -= 1

print(ans)
