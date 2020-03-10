#coding:UTF-8
class A(object):

    def __init__(self):
        self.hungry = '123'
        print 'A类的init方法'

class B(A):

    def __init__(self):
        self.sound = '456'
        super(B, self).__init__()
        # A.__init__(self)
        # print 'B类的init方法'

if __name__ == '__main__':
    # a  = A()
    # print a.hungry
    b = B()
    print b.sound
    print b.hungry
    print B.mro()