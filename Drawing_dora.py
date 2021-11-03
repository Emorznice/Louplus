from turtle import *

# 设置窗口大小
setup(500, 500)
# 设置画笔
speed(10)
shape('turtle')
colormode(255)

# 绘制圆
def drawRound(size, filled):
    pendown()
    if filled == True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled == True:
        end_fill()

# 绘制矩形
def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled == True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled == True:
        end_fill()

# 绘制头部
def head():
    # 绘制大圆
    color('blue', 'blue')
    penup()
    goto(0, 100)
    drawRound(75, True)
    # 绘制小圆
    color('white', 'white')
    penup()
    goto(0, 72)
    drawRound(60, True)

# 绘制眼睛
def eyes():
    # 左眼框
    color('black', 'white')
    penup()
    goto(-15, 80)
    drawRound(17, True)
    # 右眼框
    color('black', 'white')
    penup()
    goto(19, 80)
    drawRound(17, True)
    # 左眼珠
    color('black', 'black')
    penup()
    goto(-8, 70)
    drawRound(6, True)
    color('white', 'white')
    penup()
    goto(-8, 66)
    drawRound(2, True)
    # 右眼珠
    color('black', 'black')
    penup()
    goto(12, 70)
    drawRound(6, True)
    color('white', 'white')
    penup()
    goto(12, 66)
    drawRound(2, True)

def nose():
    color('red', 'red')
    penup()
    goto(0, 40)
    drawRound(7, True)

def mouth():
    color('black', 'black')
    penup()
    goto(-30, -20)
    pendown()
    setheading(-27)
    circle(70, 55)

    penup()
    goto(0, 26)
    pendown()
    goto(0, -25)

# 胡子
def whisker():
    color('black', 'black')

    penup()
    goto(10, 5)
    pendown()
    goto(-40, 5)

    penup()
    goto(10, 5)
    pendown()
    goto(40, 5)

    penup()
    goto(-10, 15)
    pendown()
    goto(-40, 20)

    penup()
    goto(10, 15)
    pendown()
    goto(40, 20)

    penup()
    goto(-10, -5)
    pendown()
    goto(-40, -10)

    penup()
    goto(10, -5)
    pendown()
    goto(40, -10)

def body():
    # 蓝色身体
    color('blue', 'blue')
    penup()
    goto(-50, -40)
    drawRect(100, 80, True)
    # 白色肚子
    color('white', 'white')
    penup()
    goto(0, -30)
    drawRound(40, True)
    # 红色丝带
    color('red', 'red')
    penup()
    goto(-60, -35)
    drawRect(120, 10, True)
    # 白色腿
    color('white', 'white')
    penup()
    goto(15, -127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14, 180)
    end_fill()

def feet():
    # 左脚
    color('black', 'white')
    penup()
    goto(-30, -110)
    drawRound(20, True)
    # 右脚
    color('black', 'white')
    penup()
    goto(30, -110)
    drawRound(20, True)

def arms():
    # 左胳膊
    color('blue', 'blue')
    penup()
    begin_fill()
    goto(-51, -50)
    pendown()
    goto(-51, -75)
    left(70)
    goto(-76, -85)
    left(70)
    goto(-86, -70)
    left(70)
    goto(-51, -50)
    end_fill()
    # 右胳膊
    color('blue', 'blue')
    penup()
    begin_fill()
    goto(49, -50)
    pendown()
    goto(49, -75)
    left(70)
    goto(74, -85)
    left(70)
    goto(84, -70)
    left(70)
    goto(49, -50)
    end_fill()

def hands():
    # 左手
    color('black', 'white')
    penup()
    goto(-90, -71)
    drawRound(15, True)
    # 右手
    color('black', 'white')
    penup()
    goto(90, -71)
    drawRound(15, True)

def bell():
    # 铜铃
    color('yellow', 'yellow')
    penup()
    goto(0, -41)
    drawRound(8, True)
    # 花纹
    color('black', 'black')
    penup()
    goto(-10, -47)
    drawRect(20, 4, False)
    # 金属丸
    color('black', 'black')
    penup()
    goto(0, -53)
    drawRound(2, True)

def package():
    color('black', 'black')
    penup()
    goto(-25, -70)
    pendown()
    setheading(-90)
    circle(25, 180)
    goto(-25, -70)
    hideturtle()

head()
eyes()
nose()
mouth()
whisker()
body()
feet()
arms()
hands()
bell()
package()

done()
