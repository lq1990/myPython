# 描述符，
# 定义一个类，具有一定的特性比如限制set，使得此类可以 作为其他类的类属性

class Sign:

    def __init__(self, val=1):
        self.val = val

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if value in [1,2,3,4,5,6]:
            self.val = value
        else:
            print("error")

    def __delete__(self, instance):
        pass

