import turtle as trtl 
import process_img
import animates
import turtle_test

# temporary jpeg to gif converter
process_img.convert_to_gif(['5.jpg'])

# how many unique pictures do you have?
pict_number = 5

# init color palets
colors = [
[(96,60,20,255),(212,91,18,255),(243,188,46,255),(95,84,38,255),(156,39,6,255)],

[(215,38,49,255),(162,213,198,255),(7,123,138,255),(92,60,146,255)],

[(173,116,96,255),(136,56,45,255),(168,74,92,255),(214,163,84,255),(245,213,188,255),(249,227,203,255)],

[(55,53,54,255),(240,77,57,255),(240,185,45,255),(243,212,135,255)],

[(255,255,255,255),(0,0,0,255)]
]
# prompt image selection
choice = input('choose a number 1-25', )
choice = int(choice)-1
choice_mod = str(choice%pict_number+1)
# make backgrounds
bg1 = process_img.BackgroundImg(''+choice_mod+'.gif', colors[choice//pict_number])

# convert choice into a string
path1 = bg1.path
print('start bg:', path1)

bg1.cell_shade()
bg1.save()

# turtle related operations: make screen, sample image, draw using turtles
wn = trtl.Screen()
wn.colormode(255)
wn.bgpic(choice_mod+'.gif')
samples = bg1.sample_coords(int(input('please select the number of turtles that will appear to convert the image, a number between 2000-3000 is recommended: ')))
SampleTurts = animates.SampleTurtles(samples)
SampleTurts.t_stamp(float(input('please select the size of turtles [.1 to .3 recommended]: ')), input('please select the shape of the turtle -- circle, turtle, and square are tested: '))
#wn.clear()
#wn.bgpic('cs_' + path1)
wn.bgpic('nopic')
#SampleTurts.t_stamp(.1, 'circle')





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
