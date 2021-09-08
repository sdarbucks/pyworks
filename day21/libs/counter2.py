class Counter:
    x = 0  #클래스 변수
    
    def __init__(self):  #초기 생성자
        Counter.x += 1

    def __str__(self):  #객체의 정보 출력
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)


