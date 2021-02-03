
class Singleton:
    def __init__(self, x=0):
        self.x = x


sc = Singleton()

def fn():
    print(sc.x)
    sc.x = 10
    print(sc.x)

def fn2():
    print(sc.x)
    sc.x = 20
    print(sc.x)

if __name__ == '__main__':
    fn()
    fn2()


