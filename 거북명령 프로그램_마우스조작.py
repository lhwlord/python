import turtle
import random

#함수선언부
def screenLeftClick(x, y):
    global r, g, b # 밖에 선언된 전역변수 쓰려고 가져옴
    turtle.pencolor((r,g,b)) # 임의색 지정하는 라이브러리 전용함수. 이중괄호는 튜플에 해당하며, 리스트와 다르게 값이 안바뀜
    turtle.pendown() # 펜내려서 그려라
    turtle.goto(x,y) # 그대로 좌표이동(마우스 따라가는건 라이브러리에서 처리)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r, g, b = random.random(), random.random(), random.random()


#변수선언부
pSize = 10
r, g, b = 0.0, 0.0, 0.0

#메인코드부
turtle.title('거북이로 그림그리기')
turtle.shape('turtle') # 커서가 거북이로 바뀐다
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
