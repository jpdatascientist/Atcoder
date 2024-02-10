
#S = OXXOXOOXOX  n = 10 k = 3
#oの数がK回に達するとその後のoをxに変える





n,k = map(int,input().split())
S = list(input())

for i in range(k):
    if S[i] == "o":
        if k  <= 0:
            S[i] = "x"
        k -= 1