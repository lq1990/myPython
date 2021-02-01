from review.clz.Sign import Sign


class Box():
    __count = 0
    sign = Sign()

    def __init__(self, len=0, wid=0, hei=0):
        self.length = len
        self.width = wid
        self.height = hei
        self.__vol = len * wid * hei
        self._color = ''
        self._isOpend = False
        Box.__count += 1
        self.sign1 = Sign()

    def __call__(self, *args, **kwargs):
        return self.__vol

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        self._color = val

    def get_count(self):
        return Box.__count

    def get_vol(self):
        return self.__vol

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def open(self):
        if(not self._isOpend):
            self._isOpend = True
            print("this box is now opened!")
        else:
          print("this box is already opened, can not open it again!")

    def close(self):
        if(self._isOpend):
            self._isOpend = False
            print("this box is now closed!")
        else:
          print("this box is already closed, can not close it again!")


if __name__ == '__main__':
    pass

b1 = Box(1,2,3)

print(b1.get_vol())
print(b1.get_count())

b2 = Box(2,3,4)
print(b2.get_vol())
print(b2.get_count())

b3 = Box()
print(b3.get_vol())
print(b3.get_count())

print("sign:")
print(b3.sign)
b3.sign = 3
print(b3.sign)

print("call:")
print(b3())


