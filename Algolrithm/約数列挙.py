n = 100
ans = []
def yakusu(a):
    A = int(n ** 0.5)
    for i in range(1,A+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    return sorted(ans)

print(yakusu(n))

