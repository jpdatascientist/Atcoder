
#133　　　不完全！！！！！！
#N個のアイテムから条件に合う２個のものを選ぶ時、条件を満たすものが何個あるか数える問題
#平方根を計算する問題　二次元配列の使い方.平方根の使い方をマスター

N,D = map(int,input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

# N=3 
# D=2  
# A=[[1,2][5,5][-2,8]]

#与えられた整数が平方根かどうかを調べる関数
def square (a):
    return int(a ** 0.5) ** 2 == a

ans = 0
for i in range(N):
    for j in range(i+1,N):
        dd = 0
        for d in range(D):
            dd += abs(A[i][d] - A[j][d]) 

            if square(dd):
                ans += 1



