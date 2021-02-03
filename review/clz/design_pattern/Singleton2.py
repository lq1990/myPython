
class Singleton2:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_sgl'):
            cls._sgl = super().__new__(cls, *args, **kwargs)
        return cls._sgl


if __name__ == '__main__':
    s1 = Singleton2()
    s2 = Singleton2()
    print(id(s1))
    print(id(s2))
    # 两者是一样的id

