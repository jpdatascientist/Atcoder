# https://atcoder.jp/contests/abc237/tasks/abc237_b
#行列転置の問題

h,w = map(int,input().split())

ar = []
for i in range(h):
    a = list(map(int,input().split()))
    ar.append(a)

# ans = []
# for j in range(w):
#     a = []
#     for i in range(h):
#         a.append(ar[i][j])
#     ans.append(a)

#この一行はこのように書いた方が簡単
ans = [[ar[i][j] for i in range(h)] for j in range(w) ]

for i in ans:
    print(*i)