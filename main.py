import turtle as trtl 
import numpy as np
import requests
from skimage import data
from skimage.io import imread, imshow
import pygame


# posting a local image file:
def import_imgs():
  r = requests.post(
      "https://api.deepai.org/api/deepdream",
      files={
          'image': open('Boston-Public-Garden.jpg', 'rb'),
      },
      headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
  )
  print(r.json())

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('fall turtle course!')
clock = pygame.time.Clock()
FPS = 20

end = False

#enter main input detecting loop

while not end:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      end = True
      print(str(event).split(' ')[0].split('-')[1])
  

  pygame.display.update()
  clock.tick(FPS)

# end pygame
pygame.quit()

# tests inputs
def test0():
  pass
