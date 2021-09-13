# 마음대로 걷는 거북이

import  turtle as t
import random

t.shape('turtle')
t.speed(0)
t.bgcolor("yellow")
t.color("purple")
t.pensize(30)
for x in range(5000):
    angle = random.randint(1, 360)  # 1~360도 랜덤한 각도
    t.setheading(angle)
    t.forward(30)
