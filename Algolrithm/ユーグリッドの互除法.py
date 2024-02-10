a,b = 33,88
def gcd(A,B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A # A < Bの場合、大きい方Bを書き換える
        else:
            A = A % B # A > Bのばいい、大きい方Aを書き換える
    #片方が０になったら操作を終了する。もう片方の数が最大公約数である。

    if A >= 1:
        return A
    
    return B

print(gcd(a,b))

#複数個の最大公約数を計算する
#N個の正の整数A1,A2,...ANの最大公約数を計算する

