# 여러개의 원 그리기
import turtle as t

n = 50
t.speed(0)  #최고 속도 (1~10)
t.bgcolor('black')
t.color('green')
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.forward(100)
t.color('pink')
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.mainloop()