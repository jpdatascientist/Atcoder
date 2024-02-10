#https://atcoder.jp/contests/abc303/tasks/abc303_a



def is_amatch(c,d):
    return(
        c == d
        or (c == "1" and d == "l")
        or (c == "l" and d == "1")
        or (c == "0" and d == "o")
        or (c == "o" and d == "0")
    )

def ans_match(s,t):
    for i in range(n):
        if not is_amatch(s[i],t[i]):
            return False
        
    return True

n = int(input())
s = input()
t = input()
print("Yes" if ans_match(s,t) else "No")
