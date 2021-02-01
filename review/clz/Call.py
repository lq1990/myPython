# 使得实例 可以像 方法一样，被调用

class Test:
    def __call__(self, *args, **kwargs):
        print("call...")


if __name__ == '__main__':
    t = Test()
    t()

