# https://atcoder.jp/contests/abc301/tasks/abc301_b

n = int(input())
a = list(map(int, input().split()))

# n = 4
# a = 2 5 1 2

while True:
    if all(abs(a[i] - a[i + 1]) == 1 for i in range(n - 1)):
        break

b = []
for i in range(n-1):
    if a[i] <= a[i+1]:
        #listに対してのrangeも可能　a[i]から[i+1]までをlistにして代入
        b += list(range(a[i],a[i+1]))
    if a[i] >= a[i+1]:
        b += list(range(a[i],a[i+1],-1))
