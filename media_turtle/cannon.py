# 거북이 대포 게임
import turtle as t
import random


def turn_up():
    t.left(2)  # 왼쪽으로 2도 돌림


def turn_down():
    t.right(2)  # 오른쪽으로 2도 돌림


def fire():
    ang = t.heading()    # 현재 거북이의 머리 각도
    while t.ycor() > 0:  # 거북이가 땅위에 있는 동안 ycor() -> coordinate(좌표)
        t.forward(15)    # 15만큼 이동하면서 우측으로 5도 만큼 변경
        t.right(5)
        
    # 거북이가 땅에 닿음
    d = t.distance(target, 0)  # 거북이와 목표 지점까지의 거리
    t.sety(random.randint(10, 100))  # 문자열을 출력할 y좌표
    if d < 25:  # 과녁에 명중하면
        t.color('blue')
        t.write("Good", False, "center", ("", 17))
        # t.write(문자열, 위치고정, 정렬위치, 글꼴 크기)
    else:
        t.color('red')
        t.write("Bad", False, "center", ("", 15))
        t.color('black')
        t.goto(-200, 10)  # 처음 위치로 돌아가기
        t.setheading(ang)  # 처음각도로 재설정함

# 땅을 그린다.
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점
target = random.randint(50, 150)  # x축 과녁
t.color('green')
t.pensize(3)
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 거북이 위치 설정
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

# 키보드 조종
t.onkeypress(turn_up, "Up")  # 키보드를 누를 때에만 실행될 수 있도록 turn_up 뒤에 ()를 뺀다.
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")  # space는 소문자로 입력

t.listen()

t.mainloop()
