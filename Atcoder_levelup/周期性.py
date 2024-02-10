#問題文通りに行うとTLEしてしまう 周期性を利用する
#A を 10** 100回連結した数列を数列Bとします。
"""B の項を前から順に足したとき、和が初めて X を超えるのは何項目まで足したときですか？
すなわち、以下の式を満たす最小の整数 
k を求めてください"""

n = int(input())
a = list(map(int,input().split()))
x = int(input())

a_sum = sum(a)
#まずaが最低幾つ必要か
quo = x // a_sum
#項数　商　＊　aの要素数
k = quo * n
#合計　aの個数　＊　aの合計
b_sum = quo * a_sum

for i in range(n):
    b_sum += a[i]
    k += 1
    
    if x < b_sum:
        print(k)
        
        exit()
        
