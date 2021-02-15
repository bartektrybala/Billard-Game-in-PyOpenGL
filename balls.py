from OpenGL.GLU import *
import numpy as np
import random
from math import *

# klasa pomocnicza, pozwalająca na odwoływanie się do słowników przez notację kropkową
class dd(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


colors = np.array(
    [[1, 1, 0],  #yellow
     [0, 0, 1],  #blue
     [1, 0, 0],  #red
     [0.4, 0, 0.8],  #violet
     [1, 0.5, 0],  #orange
     [0, 0.4, 0],  #dark green
     [0.6, 0, 0],  #dark red
     [0, 0, 0],  #black
     [1, 1, 0],  # yellow
     [0, 0, 1],  # blue
     [1, 0, 0],  # red
     [0.4, 0, 0.8],  # violet
     [1, 0.5, 0],  # orange
     [0, 0.4, 0],  # dark green
     [0.6, 0, 0]])  # dark red

velo = np.array(
    [[1, 0, 2],
     [2, 0, 1],
     [-1, 0, 1],
     [-2, 0, -2],
     [-5, 0, 0],
     [2, 0, 1],
     [2, 0, 2],
     [3, 0, 4]])

sr = -6
r = 0.4
position = np.array(
    [[0, r, sr],
     [-r, r, sr-sqrt(3)*r],
     [r, r, sr-sqrt(3)*r],
     [-2*r, r, sr-2*sqrt(3)*r],
     [0, r, sr-2*sqrt(3)*r],
     [2*r, r, sr-2*sqrt(3)*r],
     [-3*r, r, sr-3*sqrt(3)*r],
     [-r, r, sr-3*sqrt(3)*r],
     [r, r, sr-3*sqrt(3)*r],
     [3*r, r, sr-3*sqrt(3)*r],
     [-4*r, r, sr-4*sqrt(3)*r],
     [-2*r, r, sr-4*sqrt(3)*r],
     [0, r, sr-4*sqrt(3)*r],
     [2*r, r, sr-4*sqrt(3)*r],
     [4*r, r, sr-4*sqrt(3)*r]])


balls = []
for i in range(15):
    part = {}
    part = dd(part)
    part.v = [0, 0, 0]
    part.p = position[i]
    part.m = 10
    part.r = r
    part.col = colors[i]
    part.quad = gluNewQuadric()
    balls.append(part)