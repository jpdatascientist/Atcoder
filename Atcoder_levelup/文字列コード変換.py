# a,b,c・・・のコードは97,98,99となっている
a = list(map(int, input().split()))
ans = ""
for i in range(26):
    ans += chr(a[i] + 96)
print(ans)
