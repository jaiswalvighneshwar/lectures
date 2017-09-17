class A(object):

    def __init__(self):
        print "Init of A"

    def fun(self):
        print "Fun"

    def hi(self):
        print "Hi of A"
object

class B(object):
    def __init__(self):
        print "Init of B"

    def hello(self):
        print "Hello"

    def hi(self):
        print "Hi of B"

class C(B,A):
    def __init__(self):
        super(C,self).__init__()

if __name__ == '__main__':
    c=C()
    c.fun()
    c.hello()
    c.hi()
    d = A()
    c  = d
    c.hi()
