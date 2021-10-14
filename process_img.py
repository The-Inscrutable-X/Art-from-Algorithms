import numpy as np
import requests
from skimage import data
from skimage.io import imread, imshow
from urllib.request import urlretrieve
from PIL import Image

path = ['test_import.png']

for i in path:
  if i.endswith('.jpg') or i.endswith('.png'):
    img = Image.open(i)
    img.save(i.split('.')[0]+".gif")

class BackgroundImg:
  # posting a local image file:
  def __init__(self, path):
    self.path = path
    self.image = imread(self.path)

    # debugging, turns off deepai usage
    if False:
      with open(path, 'rb') as pic:
        r = requests.post(
            "https://api.deepai.org/api/deepdream",
            files={
                'image': pic,
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
      print(r.json())
      try:
        urlretrieve(dict(r.json())['output_url'], '_dreamed'+path)
      except:
        print('key broken')

  # show image file on screen
  def show(self):
    imshow(self.path)

  def clamp(pixel):
    pass

    


