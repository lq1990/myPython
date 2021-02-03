# 策略模式
# 把类作为参数

class Moveable:
    def move(self):
        print("moving...")


class MoveOnFeet(Moveable):
    def move(self):
        print("move on feet...")


class MoveOnWheel(Moveable):
    def move(self):
        print("move on wheels...")


class MoveObj:
    def set_move(self, Clz): # pass Clz as param
        self.moveable = Clz()

    def move(self):
        self.moveable.move()


if __name__ == '__main__':
    m = MoveObj()

    m.set_move(Moveable)
    m.move()

    m.set_move(MoveOnFeet)
    m.move()

    m.set_move(MoveOnWheel)
    m.move()


