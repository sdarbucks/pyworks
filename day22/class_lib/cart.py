# 장바구니 클래스 만들기
class Cart:
    def __init__(self, goods):
       self.li = []
       self.li.append(goods)

    def __str__(self):
        print(self.goods)

c1 = Cart("계란")
print(c1.li)
c2 = Cart("두부")
print(c2.li)
c3 = Cart("커피")
print(c3.li)
