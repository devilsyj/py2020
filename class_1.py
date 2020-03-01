#coding:UTF-8
import inspect
class Fruit:
    price = 0    #类属性(静态变量，可以直接被类调用不需实例化)，类和实例都可以访问

    def __init__(self):
        self.__color = 'red'   #实例属性，访问必须先实例化
        self.num = 100

    def counter(self):
        self.price += 1

    def funcname(self):
        return inspect.stack()[1][3]
        print '2020'

    def test(self):
        print self.funcname()



if __name__ ==  "__main__":
    apple = Fruit()
    print apple.price
    apple.counter()
    print apple.price
    print Fruit.price
    apple.test()
    # print dir(Fruit)
    # print apple
    # n = getattr(apple,'test')
    # print type(n)
    # n()

    # print Fruit.price
    # apple = Fruit()
    # print apple.color, apple.price
    # Fruit.price += 10
    # print Fruit.price, apple.price
    # banana = Fruit()
    # print banana.price
    # dir(Fruit)
    # apple = Fruit()
    # print apple.__color    #私有属性不能直接通过实例化访问
    # print dir(Fruit())
    # print apple._Fruit__color
    # apple._Fruit__dispay()
    # n = getattr(apple,dis)

