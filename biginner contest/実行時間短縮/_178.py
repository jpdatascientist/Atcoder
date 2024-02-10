#https://atcoder.jp/contests/abc178/tasks/abc178_b

#a<=x<=b および　c<=y<=dを満たす　x＊yの最大値は何か
#範囲が広すぎる場合全探索をするとTELになってしまう
#x、yを定数として考えて場合分をシンプルに


a,b,c,d = map(int,input().split())

ans = max((a*c),(a*d))
ans2 = max((b*c),(b*d))

print(max(ans,ans2))
        
