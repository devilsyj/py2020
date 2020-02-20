#coding:UTF-8
class Fruit:
    price = 0    #类属性(静态变量，可以直接被类调用不需实例化)，类和实例都可以访问

    def __init__(self):
        self.__color = 'red'   #实例属性，访问必须先实例化



if __name__ ==  "__main__":

    # print Fruit.price
    # apple = Fruit()
    # print apple.color, apple.price
    # Fruit.price += 10
    # print Fruit.price, apple.price
    # banana = Fruit()
    # print banana.price
    apple = Fruit()
    # print apple.__color    #私有属性不能直接通过实例化访问
    print dir(Fruit())
    print apple._Fruit__color

