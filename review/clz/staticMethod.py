
class StaticMethod:
    abc = ''

    def __init__(self, f0, f1, f2=2, f3=3):
        self.f1 = f1
        self.f2 = f2

    @staticmethod
    def mul(val1, val2):
        print(StaticMethod.abc)
        return val1 * val2

    @classmethod
    def get_f1(cls, f1, f2):
        print(cls.abc) # 使用 classmethod的好处： 无论类名如何变化，cls都可以指代此类
        return cls(f1, cls.mul(f1,f2)) # use init(), use static mul(), and return instance



if __name__ == '__main__':
    # s1 = StaticMethod()
    # print(StaticMethod.mul(s1.f1, s1.f2))

    s2 = StaticMethod.get_f1(2,33)
    print(s2.f1)
    print(s2.f2)




