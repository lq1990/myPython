class Test:
    """
    docstring for test
    """

    # fields of class
    clza = 'abc'
    clzb = 1000

    def __init__(self):
        self.a = 0  # field of instance
        self.b = 10
        # __ for private
        self.__priA = 'priA1'
        self._water = ''

        # _ for protected
        self._proA = "proA1"

    # decorator, 可以 t.water 代替t.water() 来方便使用
    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, w):
        if 0 <= w <= 500:
            self._water = w
        else:
            print("set water failure")

    def info(self):
        print('a: ', self.a)
        print('b: ', self.b)



t = Test()

# print(t.__doc__)
t.info()
t.color = 'red'  # 在类的外部定义实例属性，但不建议这样做
print(t.color)
print(Test.clza)
print(t.clza)

print("特殊属性：")
print(t.__doc__)
print(Test.__dict__)
print(Test.__name__)
print(t.__module__)
print(Test.__module__)
print(Test.__base__)

print("reflect")
print(getattr(t, 'b'))
setattr(t, 'b', 66)
print(getattr(t,'b'))
print(hasattr(t, 'b'))

print("property:")
t.water = 1000
print(t.water)

