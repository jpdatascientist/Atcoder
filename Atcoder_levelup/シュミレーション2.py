# 入力の受け取り
N=int(input())
S=list(map(int, input().split()))
T=list(map(int, input().split()))

# i番目のすぬけ君が初めて宝石をもらう時間
# 初期値は大きい数
time=[10**15]*N

# 1週目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするためNで割った余りを取る
    next=(i+1)%N
    # 高橋君からもらうのが早いか、隣のすぬけ君からもらうのが早いか
    time[next]=min(T[next],time[i]+S[i])

# 2周目
for i in range(N):
    next=(i+1)%N
    # 1周目で計算した時間が早いか、隣のすぬけ君からもらうのが早いか
    time[next]=min(time[next],time[i]+S[i])

# 答えの出力
for i in range(N):
  print(time[i])
