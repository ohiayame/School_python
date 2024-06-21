import turtle

# 画面を設定
screen = turtle.Screen()
screen.title("Draw Circle from Top")

# カメを作成
t = turtle.Turtle()

# カメの方向を90度に設定（上向き）
t.setheading(180)

# 円を描く
t.circle(50)

t.circle(40)

t.circle(30)# 半径50の円を描く

# 描画を終了
screen.mainloop()