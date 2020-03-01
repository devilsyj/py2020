class MyClass():

    def func1(self):
        print 'func1'

    def default(self):
        print 'default'

if __name__ == '__main__':
    my = MyClass()
    str = hasattr(my, 'func1')
    print type(str)
    print str
    print '-----------------'
    str2 = getattr(my, 'func1', 'default')
    print type(str2)
    print '111', str2
    str2()
    print '-----------------'
    str3 = getattr(my, 'func2', my.default)
    print '222', str3
    str3()