import math
import numpy as np
from PIL import Image

class Enhance:
    def __init__(self, px, w, h, name):
        self.px = px
        self.w = w
        self.h = h
        self.ws = 3
        self.name = name.split('/')[-1:][0]

        self.set_kernel()
        self.enhance()

    def set_kernel(self):
        self.kernel = np.array([[-1/8,-1/8,-1/8],[-1/8,1,-1/8],[-1/8,-1/8,-1/8]])

    def convolve(self, win):
        C = 0

        for i in range(self.ws):
            for j in range(self.ws):
                C += self.kernel[i][j] * win[i][j]
        
        c = int(C)
        return (c, c, c)

    def enhance(self):
        B = math.floor(self.ws / 2)
        im = Image.new('RGB', (self.w, self.h), 0)
        p = im.load()
        window = np.zeros((self.ws, self.ws), dtype=np.single)

        for i in range(B, self.w-B):
            for j in range(B, self.h-B):
                for k in range(-B, B+1):
                    for m in range(-B, B+1):
                        window[k][m] = list(self.px[i+m, j+k])[0]
                p[i, j] = self.convolve(window)
                window[:] = 0 

        im.save('Enhance/'+self.name)