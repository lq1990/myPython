class Shape:
    def __init__(self, cvns, points):
        self.cvns = cvns # canvas
        self.points = points
        self.pid = None # id

    def delete(self):
        if self.pid:
            self.cvns.delete(self.pid) # fn of canvas


class ShapeAngles(Shape):
    def __init__(self, cvns, points, angles=(10, 170)):
        super().__init__(cvns, points)
        self.angles = {'start': angles[0], 'extent': angles[1]}


class HatTop(Shape):
    def draw(self):
        self.pid = self.cvns.create_oval(*self.points)


class HatBottom(Shape):
    def draw(self):
        self.pid = self.cvns.create_polygon(*self.points)


# 在Hat里，关联了 ht, hb
class Hat:
    def __init__(self, cvns, start_point, w,h):
        self.cvns = cvns
        self.start_point = start_point
        self.w = w
        self.h = h
        self.ht = HatTop(self.cvns, self.ht_cacu())
        self.hb = HatBottom(self.cvns, self.hb_cacu())

    def draw(self):
        self.ht.draw()
        self.hb.draw()

    def delete(self):
        self.ht.delete()
        self.hb.delete()

    def ht_cacu(self):
        r = self.h / 3 / 2
        x1 = self.start_point[0] + self.w / 2 - r
        y1 = self.start_point[1]
        x2 = x1 + 2*r
        y2 = y1 + 2*r
        return x1,y1,x2,y2

    def hb_cacu(self):
        x1 = self.start_point[0] + self.w / 2
        y1 = self.start_point[1] + self.h / 3
        x2 = self.start_point[0] + self.w / 2
        y2 = self.start_point[1] + self.h
        x3 = self.start_point[0] + self.w / 3 * 2
        y3 = y2
        return x1,y1,x2,y2,x3,y3


class Sense(ShapeAngles):
    def draw(self):
        self.pid = self.cvns.create_arc(*self.points, **self.angles)


class Face(HatTop):
    pass







