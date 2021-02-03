# 策略模式
# 把类作为参数

def moveable():
    print("moving...")


def moveOnFeet():
    print("move on feet...")


def moveOnWheel():
    print("move on wheels...")


class MoveObj:
    def set_move(self, fn):  # pass fn as param
        self.moveable = fn

    def move(self):
        self.moveable()


if __name__ == '__main__':
    m = MoveObj()

    m.set_move(moveable)
    m.move()

    m.set_move(moveOnFeet)
    m.move()

    m.set_move(moveOnWheel)
    m.move()
