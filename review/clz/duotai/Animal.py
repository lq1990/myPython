
class Animal:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + self.y + other.x + other.y

    def move(self):
        print("animal is moving...")


class Dog(Animal):
    def move(self):
        print("dog is moving...")


def move(obj):
    obj.move()

def add(a,b):
    return a+b


if __name__ == '__main__':
    a = Animal(1,2)
    d = Dog(2,3)

    move(a)
    move(d)

    print(add(a,d))

