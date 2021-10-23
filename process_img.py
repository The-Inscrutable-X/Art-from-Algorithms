import numpy as np
import requests
from skimage import data
from skimage.io import imread, imsave
from skimage.transform import rescale
from urllib.request import urlretrieve
from PIL import Image
import random

# temporary rescaling operation
#image = imread('1large.gif')
#image_rescaled = rescale(image, 0.25, anti_aliasing=False)
#imsave('1.gif', image_rescaled)

class CustomException(Exception):
  pass

# convert to gif
def convert_to_gif(path):
  for i in path:
    if i.endswith('.jpg') or i.endswith('.jpeg'):
      try:
        img = Image.open(i)
        img.save(i.split('.')[0]+".gif")
      except:
        print(i , 'does not exist, or is already converted to a gif')

class BackgroundImg:
  # posting a local image file:
  def __init__(self, path, colors):
    self.path = path
    self.image = imread(self.path)
    self.colors = colors

    # state trackers
    self.shaded = True

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

    imsave('cs_' + self.path, self.image)

    print('image saved at', 'cs_' + self.path)
    
    
  # compares a pixel and returns the closest color from self.colors, this is the key to the color clamping technique
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

    #print(self.image[0:1,0:10,:])
    self.image = np.apply_along_axis(self.pixel_clamp_cs, 2, self.image)
    #print('2nd' , self.image[0:1,0:10,:])

  # samples number amount of coords and their colors
  def sample_coords(self, number):
    shape = self.image.shape
    print(shape)
    if self.shaded == True:
      # prepare sample coords dict keyed by color
      samples = dict(zip(self.colors, [[] for i in self.colors]))
      for i in range(number):
        y = random.randint(0, shape[0]-1)
        x = random.randint(0, shape[1]-1)

        #identify color
        color = tuple(self.image[y, x, :])

        #adjust to be on top of background
        y = (-y+shape[0]/2)
        #y = -y
        x -= shape[1]/2
        # append colors
        try:
          samples[color].append((x,y))
        except KeyError as e:
          raise CustomException('cell shading incomplete') from e

    elif self.shaded == False:

      print('unshaded')
      colors = []
      coords = []
      for i in range(number):
        x = random.randint(0, shape[0])
        y = random.randint(0, shape[1])

        color = tuple(self.image[x-1, y-1, :])
        colors.append(color)
        coords.append((x,y))
      samples = dict(zip(colors, coords))

    #print(samples)
    return samples