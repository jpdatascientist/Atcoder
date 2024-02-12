"""高橋君は 7 が嫌いです。1 以上 N 以下の整数のうち、
10 進法で表しても 8 進法で表しても 
7 を含まないような数はいくつありますか？"""

# 10進数を8進数に変換する場合、以下の操作を0になるまで繰り返す。
# (1)8で割った余りを一番上の桁につける
# (2)次に割るモノを8で割った商に置き換える　この商が０になるまで繰り返す


# ①10進法で7を含むかを判定する関数
def judge_ten(x):
    x = str(x)
    if "7" in x:  # 文字列の方が簡単位判定を行えるため
        return True
    else:
        return False


# ②8進法で7を含むか判定する関数
def judge_eight(x):
    S = ""  # xの8進法表示をSとする

    while x > 0:
        S = str(x % 8) + S  # 余りを先頭へ入れる
        x //= 8

    if "7" in S:
        return True
    else:
        return False


N = int(input())

# Falseになれば7を含まないことになるので上記関数が共にFalseである場合をcountする
# 範囲は1以上Nまで調べる
count = 0
for i in range(1, N + 1):
    if judge_ten(i) == False and judge_eight(i) == False:
        count += 1
print(count)
