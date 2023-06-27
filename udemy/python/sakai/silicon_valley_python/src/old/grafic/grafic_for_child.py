import turtle
import time

# 亀のアイコンを出力
turtle.shape('turtle')
# アイコンの色を変更
turtle.color('red')
# 第二引数はアイコンのエッジの色を変更します
turtle.color('red', 'yellow')

# 前に100だけ進めます
turtle.forward(100)
# 右に90進めます
turtle.right(90)
# 亀のアイコンを隠します
turtle.hideturtle()
turtle.forward(100)
# 亀のアイコンを表示する
turtle.showturtle()

# 円を書いて進みます
turtle.circle(100)

time.sleep(2)

# 軌跡の色を変更します
turtle.pencolor('blue')
turtle.right(45)
turtle.forward(100)
# 後ろに進みます
turtle.backward(200)

#　初期位置に戻ります
turtle.home()
# タートルのクリア
turtle.clear()
# タートルの終了コマンド　
turtle.done()
