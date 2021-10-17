import numpy as np
import requests
from skimage import data
from skimage.io import imread, imsave
from urllib.request import urlretrieve
from PIL import Image
import random

# convert to gif
def convert_to_gif(path):
  for i in path:
    if i.endswith('.jpg') or i.endswith('.jpeg'):
      try:
        img = Image.open(i)
        img.save(i.split('.')[0]+".gif")
      except:
        print(i , 'does not exist')

class BackgroundImg:
  # posting a local image file:
  def __init__(self, path):
    self.path = path
    self.image = imread(self.path)
    self.colors = [(96,60,20,255),(212,91,18,255),(243,188,46,255),(95,84,38,255),(156,39,6,255)]

    # state trackers
    self.shaded = False   

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

  # save to separate file
  def save(self):
    self.image = self.image.astype(np.uint8)
    print('image data type', (type(self.image)), self.image.shape)
    imsave(('cs_' + self.path), self.image)
    

  def pixel_clamp_cs(self, pixel):

    '''
    ((r-x[0])**2)*.3+
    ((g-x[1])**2)*.59+
    ((b-x[2])**2)*.11+
    (a-x[3])**2
    
    '''

    '''
    abs((r-x[0])+
    (g-x[1])+
    (b-x[2])+
    (a-x[3]))
    '''

    '''
    ((r-x[0])**2)+
    ((g-x[1])**2)+
    ((b-x[2])**2)+
    (a-x[3])**2
    '''
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    a = pixel[3]
    distances = map(lambda x: 
    ((r-x[0])**2)*.3+
    ((g-x[1])**2)*1.59+
    ((b-x[2])**2)*.11+
    (a-x[3])**2
    , self.colors)
    distances = tuple(distances)
    #index_min = min(range(len(distances)), key=distances.__getitem__)
    index_min = np.argmin(distances)

    # make progress counter
    p_step = 5 #percentage fulfilled per print indication
    self.counter += 1
    pixels = self.image.shape[0]*self.image.shape[1]
    percent = [i for i in range(0,100,p_step) if ((self.counter/pixels)*100 == i)]
    for i in percent:
      print(self.counter,'/' , pixels, str(percent[0]) + '%')
      print(':' , distances, index_min)

    # return color of pixel
    return self.colors[index_min]

  def cell_shade(self):
    self.counter = 0
    self.shaded = True

    print(self.image[0:1,0:10,:])
    self.image = np.apply_along_axis(self.pixel_clamp_cs, 2, self.image)
    print('2nd' , self.image[0:1,0:10,:])

  # samples number amount of coords and their colors
  def sample_coords(self, number):
    shape = self.image.shape
    if self.shaded == True:
      # prepare sample coords dict keyed by color
      samples = dict(zip(self.colors, [[] for i in self.colors]))
      for i in range(number):
        x = random.randint(0, shape[0])
        y = random.randint(0, shape[1])

        color = tuple(self.image[x, y, :])
        print('sample', color)

        samples[color].append((x,y))

    elif self.shaded == False:

      print('unshaded')
      colors = []
      coords = []
      for i in range(number):
        x = random.randint(0, shape[0])
        y = random.randint(0, shape[1])

        color = tuple(self.image[x, y, :])
        colors.append(color)
        coords.append((x,y))
      samples = dict(zip(colors, coords))

    print(samples)
    return samples

