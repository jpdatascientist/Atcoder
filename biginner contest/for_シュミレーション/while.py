"""
n個の整数が与えられる。与えられた文字が2で割り切れる回数を出力する

"""

n = int(input()) #3
A = list(map(int,input().split())) #16,12,24

res = 0
while True: #以下の処理がTrueになるまで操作を続ける
    ans = False
    for i in range(n):
        if A[i] % 2 != 0: #奇数であった場合True
            ans = True
    if ans: # ans=Tureであればbreak
        break
    for i in range(n):#偶数で処理を続けられる場合
        A[i] //= 2

    res += 1


"""
 正整数 N が与えられるので1以上N以下の整数のうち、最も 2 で割れる回数が多いものを
求めてください。答えは必ず 1 つに定まります。
なお、2 で割っていき、何回あまりが出ずに割れるかを、2 で割れる回数と呼ぶことにします。
6 -> 3...1回  8 -> 4 -> 2 -> 1 ...3回
 """   
n = int(input())
total = -1 #何回割り切れたかを保存する変数
ans = -1 #その整数を保存する変数

for x in range(1,n+1):
    cnt = 0#その整数が割り切れた回数を保存する変数
    y = x #一旦変数を置いて、while分で繰り返されるように設定
    
    while y % 2 == 0:
        y //= 2
        cnt += 1
        
    if total < cnt:
        total = cnt
        ans = x 
print(ans) 


