import turtle

# 화면을 생성하여 거북이가 그릴 수 있는 캔버스를 만듦
screen = turtle.Screen()

# 그림을 그릴 거북이 객체를 생성함
t = turtle.Turtle()

# 반지름이 50인 원을 그림
t.circle(50)

# 터틀 그래픽 창이 닫히지 않고 유지되도록 함
turtle.done()