"""長さDの文字列Tがあります。"o"が連続している個数は最大で何個ですか？
o が連続している個数の最大値を記録する変数を ans とする。ans=0 である。
また、(文字列を左から見ていくとして) 今まで見た文字列の末尾に連続する o の個数を 
cur とする。はじめ cur=0 である。
T[i]= o である場合は、今まで見た文字列の末尾の o が 1 個増えるので cur を 
cur+1 に更新する。
T[i]= x である場合は、末尾が x になるので、cur を 0 に更新する。
その後、ans を max(ans,cur) に更新する。
"""


n,d = map(int,input().split())

array = []
for i in range(n):
    a = list(input())
    array.append(a)

ans = 0 #最大値を保持する変数
cur = 0 #列の全てが"o"となったら＋１されていく変数
for j in range(d): #列を今回は確かめたいので for j in range(d)
    can = 1 # 初期値TRUE
    for i in range(n):
        can &= array[i][j] == "o"  #can = can & array[i][j] == "o"
                                   #s[i][j]が"o"と等しい場合にcan変数を1に設定
    if can:
            cur += 1#列の要素が全て"o"である場合に＋1
    else:
            cur = 0#そうでない場合には０
            
    ans = max(ans,cur)#最大値を更新
print(ans)
        