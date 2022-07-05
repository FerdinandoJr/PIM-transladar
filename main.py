import numpy as np
import matplotlib.pyplot as plt
import imutils 
import cv2  
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

path = '/content/drive/MyDrive/PIM/'
verticalBars = imread(path+'verticalBars.png')
verticalBars15 = imread(path+'verticalBars15.png')
verticalBars30 = imread(path+'verticalBars30.png')
verticalBars45 = imread(path+'verticalBars45.png')
verticalBars60 = imread(path+'verticalBars60.png')
verticalBars75 = imread(path+'verticalBars75.png')
verticalBars90 = imread(path+'verticalBars90.png')


def transladar(image, horizontal=0, vertical=0):
  altura, largura = image.shape[:2]
  deslocamento = np.float32([[1, 0, horizontal], [0, 1, vertical]])
  deslocado = cv2.warpAffine(image, deslocamento, (largura, altura))
  plt.imshow(deslocado)
  plt.show()

  
vert = 10 # Transladar para Verticalmente
hori = 10 # Transladar para Horizontamente

transladar(verticalBars, vert, hori)
transladar(verticalBars15, vert, hori)
transladar(verticalBars30, vert, hori)
transladar(verticalBars45, vert, hori)
transladar(verticalBars60, vert, hori)
transladar(verticalBars75, vert, hori)
transladar(verticalBars90, vert, hori)
