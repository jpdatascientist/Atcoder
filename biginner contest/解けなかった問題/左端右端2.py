#https://atcoder.jp/contests/abc261/tasks/abc261_a
#ある正の整数の数直線上の線分で共通区間の長さを求めよ


l1,r1,l2,r2 = map(int,input().split())

L = max(l1,l2)#左端
R = min(r1,r2)#右端

print(max(0,R-L)) #マイナス部分は認めない

#区間に共通する部分がるかどうか？
a,b,c,d = map(int,input().split())

l = max(a,c)
r = min(b,d)

if r-l >= 0:#0以上であることに注意する
    print("Yes")
else:
    print("No")