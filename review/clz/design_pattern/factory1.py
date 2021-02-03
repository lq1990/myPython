class Ab:
    a = 3

class Ac:
    a = 0

class MyFactory:
    def get_instance(self, ins):
        return ins()


if __name__ == '__main__':
    fac = MyFactory()
    print(type(fac.get_instance(Ab)))
    print(type(fac.get_instance(Ac)))



