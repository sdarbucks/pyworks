# 사각형의 넓이 구하기
# 가로와 세로의 길이를 입력 받아 넓이를 계산하는 프로그램을 작성하세요.

x = input("가로의 길이 : ")
width = int(x)
y = input("세로의 길이 : ")
height = int(y)

area = width * height

print("가로 길이 : " + str(width) + 'cm')
print("세로 길이 : " + str(height) + 'cm')
print("면적 : " + str(area) + 'cm')
