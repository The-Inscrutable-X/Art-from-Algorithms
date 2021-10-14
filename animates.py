import turtle as trtl

# animate left to right
class a_left_right():
  def __init__(self, coords, shape):
    self.xs = [i[0] for i in coords]
    self.ys = [i[1] for i in coords]
    self._coords = coords
    self.turtles = [trtl.Turtle() for i in self._coords]
    for i in self.turtles:
      i.shape(shape)
      i.speed(100)
      
  def next(self):
    for x,i in enumerate(self.xs):
      self.xs[x] = i+1
    self._coords = [(self.xs[i],self.ys[i]) for i in range(len(self._coords))]

  def coords(self):
    self._coords = [(self.xs[i],self.ys[i]) for i in range(len(self._coords))]
    return self._coords