class BeDeco:
    def be_edit_fn(self):
        print("source fn...")

    def be_keep_fn(self):
        print("keep fun...")


class Decorator:
    def __init__(self, Dec): # Dec is the clz to be decorated
        self._dec = Dec()   # instance

    def be_edit_fn(self): # the same fn name
        print("start...") # 装饰器定义的“装饰”
        self._dec.be_edit_fn() # 原有的方法

    def be_keep_fn(self):
        self._dec.be_keep_fn()


if __name__ == '__main__':
    bd = BeDeco()
    bd.be_edit_fn()
    bd.be_keep_fn()

    print()
    # now decorate
    dec = Decorator(BeDeco)
    dec.be_edit_fn()
    dec.be_keep_fn()


