#https://atcoder.jp/contests/abc287/tasks/abc287_b

"""4 4
000000
123456
987111
000000
000
111
999
111"""


n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
answer = 0
for i in range(n):
  found = False #条件を満たすものがあればTrue
  for j in range(m):
    if s[i][-3:] == t[j]:
      found = True
  if found: #111が２つある場合でもここでTrueとさえしておけば、２回カウントされることはない
            #この書き方必須で覚える
    answer += 1

print(answer)


