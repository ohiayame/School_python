import random
import turtle

# 화면을 설정합니다
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")
width = screen.window_width() // 2
height = screen.window_height() // 2
print("윈도우 가로X새로", width, height)
# 거북이를 생성
t = turtle.Turtle()
t.width(30)
# 거북이가 움직이는 함수를 정의
def move_foward():
    x, y  = t.position()
    flag = False
    if width == x or height == y or -width == x or -height == y:
    #     # if width == x and 180 < t.heading() < 360:
    #     #     t.forward(100)
    #     # elif height == y and 90 < t.heading() < 240:
    #     #     t.forward(100)
    #     # elif -width == x and 0 < t.heading() < 180:
    #     #     t.forward(100)
    #     # elif -height == y and 240 < t.heading() < 90:
            flag == True
            t.forward(100)
    elif x >= 0 and y >= 0:
        if width - x <= 100 :
            t.forward(width - x)
            t.left(180)
            flag = True
        elif height - y <= 100:
            t.forward(height - y)
            t.left(180)
            flag = True
        else:
            t.forward(100)
            
    else:
        if -width - x >= -100:
            t.forward(-width - x)
            t.left(180)
            flag = True
        elif -height - y <= -100 :
            t.forward(-height - y)
            t.left(180)
            flag = True
        else:
            t.forward(100)
    
    print(x,y)
def move_backward():
    t.backward(10)
    
def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

# 펜 색깔을 검은 색으로
def change_color_black():
    t.pencolor("black")

# 펜 색깔을 검은 색으로
def change_color_red():
    t.pencolor("red")
    
# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))

def color_change_():
    if t.pencolor() == "red" :
        t.pencolor("black")  
    elif t.pencolor() == "black":
        t.pencolor("red")
# def color_change_():
#     if t.pencolor() == "red" or t.pencolor() == "black" :
#         t.pencolor("black") if t.pencolor() == "red" else t.pencolor("red")

def change_color_input():
    color_li = ["blue", "black", "yellow"]
    while True:
        print("색깔 선택: ")
        print("1. 파란색")
        print("2. 검정색")
        print("3. 노란색")
        input_value = int(input("숫자 입력"))
        
        if 1 <= input_value <= 3:
            t.pencolor(color_li[input_value - 1])
            break
        
# 키보드 이벤트를 설정
screen.listen()
screen.onkey(move_foward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_color_black, "b")
screen.onkey(change_color_red, "r")
screen.onkey(color_change_, "i")
screen.onkey(change_color_input, "t")

# 이벤트 루프를 시작)
screen.mainloop()