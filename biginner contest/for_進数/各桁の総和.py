"""
1 以上 N 以下の整数のうち、10 進法での各桁の和が 
A 以上 B 以下であるものの総和を求めてください。
"""

# 各桁の和を計算する関数
def findSumOfDigits(n):
    sum = 0
    while n > 0:  # n が 0 になるまで
        sum += n % 10  
        n //= 10
    return sum

N, A, B = map(int, input().split())
total = 0

for i in range(1, N + 1):
    sum_digits = findSumOfDigits(i)  # i の各桁の和
    if A <= sum_digits <= B:  # i の各桁の和が A 以上 B 以下かどうか
        total += i

print(total)

