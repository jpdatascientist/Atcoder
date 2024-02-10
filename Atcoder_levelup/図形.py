# 異なる頂点を持つ４点のうち３点の値が与えられるので、残りの頂点の座標を求める
# 3点のうち2点は同じであると考えると、残りの座標は答えの値と同じになる

#求める座標をx4,y4とすると

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())


if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
elif x2 == x3:
    x4 = x1
    
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
elif y2 == y3:
    y4 = y1
print(x4,y4)