
class Custom:
    def __init__(self):
        print("init method.")

    def __new__(cls, *args, **kwargs):
        print("new instance")
        return object.__new__(cls, *args, **kwargs)


if __name__ == '__main__':
    print(Custom())