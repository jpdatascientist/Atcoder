#貪欲法は前後状態を考えずに、今一番良いものを取り続ける方法
#問題を見たときにまず、貪欲法で解けないかを考え、ないなら別の方法

#本問題の場合おいしさが最大の物を乗せ続ける

n,w = map(int,input().split())

cheese = []
for i in range(n):
    a,b = map(int,input().split())
    cheese.append([a,b])

cheese.sort(reverse=True)

ans = 0 #おいしさ
for i in range(n):
    deli = cheese[i][0]
    weight = cheese[i][1]
    
    if weight <= w:
        ans += deli * weight
        w -= weight
    else:
        ans += deli * w #これ以上載せられない
        
        break
        
print(ans)
        
#for文１回目のループで処理が終了後また０からループが回る？
