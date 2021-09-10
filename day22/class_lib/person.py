# Person 클래스
class Person:
    # 매개변수가 있는 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person):   # Person을 상속받음
    pass

emp1 = Employee("흥부", 30)
print(emp1.name)   #name이 Person의 소속인데 Employee 객체가 사용
print(emp1.age)
print(emp1)











"""
p1 = Person("흥부", 29)
print(p1)

p2 = Person("놀부", 33)
print(p2)
"""