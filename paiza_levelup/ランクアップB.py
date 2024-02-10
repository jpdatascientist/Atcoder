number_array = [
    ["7", "7", "7", "7"],
    ["2", "2", "2", "9"],
    ["5", "5", "6", "6"],
    ["2", "6", "6", "9"],
    ["1", "6", "8", "9"],
    ["1", "3", "3", "3"],
    ["1", "1", "8", "9"],
    ["3", "5", "8", "8"],
]
# 要素の中の数字がいくつ揃っているか判定するコード


for number in number_array:
    count = {}
    for i in range(4):
        if number[i] not in count:
            count[number[i]] = 1
        else:
            count[number[i]] += 1
    if 4 in count.values():
        print("Four Card")
    elif 3 in count.values():
        print("Three Card")
    elif len(count) == 2:
        print("Two Pair")
    elif len(count) == 3:
        print("One Pair")
    else:
        print("No Pair")

# 運賃計算
n, m = map(int, input().split())

train = []
for i in range(n):
    a = list(map(int, input().split()))
    train.append(a)


b = int(input())


y = 0
ans = 0
for i in range(1):
    k, l = map(int, input().split())
    y = l
    ans += train[k - 1][y - 1]

for i in range(b - 1):
    g, h = map(int, input().split())
    if y == h:
        y = h
    else:
        ans += abs(train[g - 1][h - 1] - train[g - 1][y - 1])
        y = h

print(ans)
