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

class SampleTurtles():
  def __init__(self, samples):
    self.samples = samples
    self.colors = []
    print(f'Brace! Turtles will appear')
  def make_gen(self):
    pass

  # make and stamp pixels, shape and size are arguments
  def t_stamp(self, turtle_size, turtle_shape):

    color_turtles = []
    #print('in t_stamp')
    for color in self.samples:
      turtle = trtl.Turtle()
      turtle.color(color[0:3])
      turtle.shape(turtle_shape)
      turtle.speed(100000)
      turtle.resizemode("auto")
      #turtle.pensize(.1)
      turtle.shapesize(turtle_size)
      turtle.penup()
      color_turtles.append(turtle)
      self.colors.append(color)
      #print('self samples', self.samples)
    #print(color_turtles)

    color_cycle = 0
    while True:
      if len(color_turtles) == 0:
        print('breaking')
        break
      for i, turtle in enumerate(color_turtles):
        #print('looping')
        try:
          turtle.goto(self.samples[self.colors[i]][color_cycle])
          turtle.right(50)
          #print('stamping')
          turtle.stamp()
          #print(coord)

        # if it isn't in the index destroy the turle, its job is done
        except:
          color_turtles.remove(turtle)
          #print('removing')
      color_cycle += 1