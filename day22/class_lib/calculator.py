# 교재 262p Q1
# Calculator 클래스 정의

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):  #외부에서 값을 입력하면 더하는 함수
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value
"""
cal1 = Calculator()
print(cal1.add(10))
"""
# UpgradeCalculator() 테스트
cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))

print(cal.value)