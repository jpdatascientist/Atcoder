# https://atcoder.jp/contests/abc134/tasks/abc134_b

"""
カバーできる範囲は[i-D,i+D]なので、2D+1の範囲をカバーできる。
よって、len=2D+1とすると、N/Dの切り上げが必要な監視員の最少人数となる。
"""
n,d = 6,2

len = 2 * d + 1
print(n + len -1 // len)