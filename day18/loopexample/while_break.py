# 무한반복 - while ~ break문
# 1부터 10까지 출력 
# Tip. 무한반복 탈출 단축키 - Ctrl + C

i = 0
while True:
    i += 1
    if i > 10:  # i가 11인경우 빠져나옴
        break
    print(i)
