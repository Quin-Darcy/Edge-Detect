import math
import numpy as np
from PIL import Image

class Edge:
    def __init__(self, px, w, h, name, ws=3):
        self.px = px
        self.w = w
        self.h = h
        self.ws = 3
        self.name = name.split('/')[-1:][0]
        self.threshold = 0.05

        self.set_kernel()
        self.get_edges()

    def set_kernel(self):
        self.kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        self.kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    def convolve(self, win):
        G_x = 0
        G_y = 0

        for i in range(self.ws):
            for j in range(self.ws):
                G_x += self.kernel_x[i][j] * win[i][j]
                G_y += self.kernel_y[i][j] * win[i][j]

        return math.sqrt(G_x**2 + G_y**2) / 1081.9

    def get_edges(self):       
        im = Image.new('RGB', (self.w, self.h), 0)
        p = im.load()
        window = np.zeros((self.ws, self.ws), dtype=np.single)

        for i in range(1, self.w-1):
            for j in range(1, self.h-1):
                for k in range(-1, 2):
                    for m in range(-1, 2):
                        window[k][m] = list(self.px[i+m, j+k])[0]
                G = self.convolve(window)
                if (G > self.threshold):
                    p[i, j] = (255,255,255)
                window[:] = 0 

        im.save('Edge/'+self.name)