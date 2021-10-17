import turtle as trtl 
import process_img
import animates
import turtle_test

process_img.convert_to_gif(['2p.jpeg'])

# make backgrounds
bg1 = process_img.BackgroundImg('2p.gif')
path1 = bg1.path

# test viewing port
#bg1.cell_shade()
bg1.sample_coords(10)
bg1.save()
path1 = 'cs_' + bg1.path

# setup screen
wn = trtl.Screen()
print('start bg:', path1)

wn.bgpic(path1)
print('done')
#image = "test_import.png"
#wn.addshape()

# test case
#Turt = trtl.Turtle()
#Turt.color('blue')
#Turt.turtlesize(2)
#turtle_test.move(Turt)

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
