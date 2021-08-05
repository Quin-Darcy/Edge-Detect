import math
import numpy as np
from PIL import Image

class Edge:
    def __init__(self, px, w, h, ws, name):
        self.px = px
        self.w = w
        self.h = h
        self.ws = ws
        self.name = name

    def set_kernel(self):
        self.kernel_x = np.array([[1, 0, -1], [2, 0, -1], [1, 0, -1]])
        self.kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    


        
