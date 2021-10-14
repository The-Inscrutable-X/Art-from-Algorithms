import turtle as trtl 
import process_img
import animates

# make backgrounds
bg1 = process_img.BackgroundImg('test_import.gif')
path1 = bg1.path

# setup screen
wn = trtl.Screen()
print('start bg:', path1)

wn.bgpic(path1)
print('done')
#image = "test_import.png"
#wn.addshape()

# test case
Turt = trtl.Turtle()
Turt.forward(1)

# animate three squares
'''
tri = a_left_right([(1,10),(2,20),(3,30)], 'square')
for i in range(100):
  tri.next()
  for x,i in enumerate(tri.coords()):
    tri.turtles[x].penup()
    tri.turtles[x].goto(i)
'''

# tests inputs
def test0():
  pass

wn.mainloop()
