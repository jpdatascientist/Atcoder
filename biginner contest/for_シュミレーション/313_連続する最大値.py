#全ての"o"かor "x"を確かめる、連続しているかしていないかを特定の変数へ代入
#その変数(文字列)のoが連続しているのは最大で何個か

n,d = map(int,input().split())
a = []
for i in range(n):
    a.append(list(input()))
    
t = ""  #  全て"o"だったら、"o" そうでなければ"x"
for j in range(d):
    #ok = all(a[i][j] == "o"  for i in range(n) )
    # if ok:
    #     t += "o"
    # else:
    #     t += "o"
    ok = 0
    for i in range(n):
        if a[i][j] == "o":
            ok += 1
    if ok == n:
        t += "o"
    else:
        t += "x"
        
#個数の最大値を更新する
ans = 0
now = 0
for i in range(d):
    if t[i] == "o":
        now += 1
    else:
        now = 0
    #連続する日の最大値を更新    
    ans = max(ans,now)
    
print(ans)