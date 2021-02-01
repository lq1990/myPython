# 自定义元类
# 元类作用： 为类指定模板。感觉上是对类又抽象了一层

class MyMeta(type):
    def __init__(self, name, bases, dicts):
        super().__init__(self)
        print("init instance...")

    def __new__(cls, name, bases, dicts):
        # 元类方法
        dicts['info'] = lambda self, val: print('val: ' + val, ', class name: ' + name)

        res = type.__new__(cls, name, bases, dicts)
        # 元类属性
        res.company = 'ABC'
        return res


class Custom(metaclass=MyMeta):
    pass


if __name__ == '__main__':
    c1 = Custom()
    c1.info('aaa')
    print(c1.company)

