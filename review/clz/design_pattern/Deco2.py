# 装饰器模式
# 使用py的注解

def deco(Clz):
    class NewClass:
        def __init__(self,age,color):
            self.wrapped = Clz(age) # construct an instance
            self.color = color
        def display(self):
            print(self.color)
            print(self.wrapped.age)

    return NewClass # return new decorated class


# 用deco 对Cat进行装饰
@deco
class Cat:
    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)


if __name__ == '__main__':
    c = Cat(12, 'black')
    c.display()
    '''
    black
    12
    '''


