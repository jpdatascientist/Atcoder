
# 碁盤の目
h,w = map(int,input().split())
array = [list(input()) for  i in range(h)]
y,x = map(int,input().split())

def flip (y,x):
    if 0 <= y and y < h and 0 <= x and x < w:
        if array[y][x] == ".":
            array[y][x] = "#"
        elif array[y][x] == "#":
            array[y][x] = "."


flip(y,x)#ここで反転させているので、下記のループは自身を含まない形でループ
for i in range(1,h): #上方向 とりうる全ての要素に対してフィリップさせる
    flip(y-i,x)
for i in range(1,h):#下方向
    flip(y+i,x)
for i in range(1,w):#左方向
    flip(y,x-i)
for i in range(1,w): #右方向
    flip(y,x+i)

for i in range(1,max(h,x)):
    flip(y-i,x+i) #斜め右上
for i in range(1,max(h,x)):
    flip(y-i,x-i) #斜め左上
for i in range(1,max(h,x)):
    flip(y+i,x-i) #斜め左下
for i in range(1,max(h,x)):
    flip(y+i,x+i) #斜め右下



for i in range(h):
    for j in range(w):
        print(array[i][j], end="")
    print()
