# 1증가하는 Counter 클래스 정의
class Counter:
    def __init__(self):  #초기 생성자
        self.x = 0    #인스턴스 변수
        self.x += 1

    def __str__(self):  #객체의 정보 출력
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)