#https://atcoder.jp/contests/abc208/tasks/abc208_b

from math import factorial#階乗

p = int(input())
ans = 0

for i in range(10,0,-1):#大きい方から硬貨を使っていく
    while factorial(i) <= p:#もしPが硬貨より大きかったらその硬貨を使い続ける
        ans += 1
        p-= factorial(i)
    
print(ans)