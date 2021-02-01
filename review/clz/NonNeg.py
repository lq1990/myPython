# 描述符的使用
# 构建类，方便统一使用

class NonNeg:

    def __init__(self, default=0):
        self.default = default

    def __get__(self, instance, owner):
        return self.default

    def __set__(self, instance, value):
        if value > 0:
            self.default = value
        else:
            print("error")

    def __delete__(self, instance):
        pass


# 把NonNeg 作为另一个类的类属性
class Movie:
    rating = NonNeg() # rating should be non negative
    score = NonNeg()


if __name__ == '__main__':
    m = Movie()
    print(m.rating)
    print(m.score)

    # m.rating = -10
