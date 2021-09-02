"""
도형의 넓이 계산하기
  1. 한 변의 길이가 5cm인 정사각형의 넓이
  2. 한 변의 길이가 5cm이고, 높이가 7cm인 삼각형의 넓이 
"""

#정사각형의 넓이
size = 8

#계산 넓이 = 가로 * 세로 
area = size * size

print("정사각형의 넓이 : ", area)

#삼각형의 넓이
width = 10
height = 20

#계산 넓이 = 밑변 x 높이 / 2
area = (width * height) / 2
print("삼각형의 넓이 : ", area)
