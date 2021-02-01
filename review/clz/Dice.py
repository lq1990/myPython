
class A:
    def af(self):
        pass


class Dice(A):

    colorNum = {'c1':1, 'c2':2, 'c3':3, 'c4':4, 'c5':5, 'c6':6}

    def __init__(self):
        pass

    def df(self):
        super().af()


    @staticmethod
    def compute_sum2(c1, c2):
        return Dice.colorNum[c1] + Dice.colorNum[c2]

    @classmethod
    def get_dice(cls):
        return Dice()


if __name__ == '__main__':
    print(Dice.compute_sum2('c1', 'c3'))
    d1 = Dice.get_dice()
    print(d1)
    print()
    print(Dice.__bases__)

    print(isinstance(Dice, type))






