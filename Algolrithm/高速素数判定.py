N = 53

def sosu (N):
    A = int(N ** 0.5)
    for i in range(2,A+1):
        if N % i == 0:
            return False
        
    return True
if sosu(N):
    print("YES")
else:
    print("NO")
    