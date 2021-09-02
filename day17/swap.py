"""
변수 blue에 1이 저장되어 있고, red에 2가 저장되어 있을때 새로운 변수
yello를 사용하여 값을 교환해 보세요
"""

#대입연산자를 활용한 변수 교환 
blue = 1
red = 2
print("교환전: ")
print("blue =", blue, ", red =", red)

#교환 처리
"""
yello = red
red = blue
blue = yello
"""

# 임시 변수 없이 바로 맞교환
blue, red = red, blue

print("교환후: ")
print("blue =", blue, ", red =", red)
