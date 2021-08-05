import math
import numpy as np
from PIL import Image

class Blur:
    def __init__(self, px, w, h, ws, name, var=0):
        self.px = px
        self.w = w
        self.h = h
        self.ws = ws # Window size
        self.name = name
        self.base_name = name.split('/')[-1:][0]
        self.var = var # Variance

        self.set_kernel()
        self.blur()

    def set_kernel(self):
        B = math.floor(self.ws / 2)
        if (self.var == 0):
            vals = [2*(a**2) for a in range(B+1)]
            var = sum(vals) / self.ws
        else:
            var = self.var

        norm_const = 2

        self.kernel = np.zeros((self.ws, self.ws))
        
        for i in range(-B, B+1):
            for j in range(-B, B+1):
                self.kernel[i+B][j+B] = norm_const * math.exp(-((j**2)/(2*var)) - ((i**2)/(2*var)))

    def convolve(self, win):
        C = np.zeros((self.ws, self.ws))
        
        for i in range(self.ws):
            for j in range(self.ws):
                C[i][j] = self.kernel[i][j] * win[i][j]

        c = int((np.sum(C) / self.ws**2))
        
        return (c, c, c)

    def blur(self):
        B = math.floor(self.ws / 2)
        im = Image.new('RGB', (self.w, self.h), 0)
        p = im.load()

        window = np.zeros((self.ws, self.ws), dtype=np.uintc)
        for i in range(B, self.w-B):
            for j in range(B, self.h-B):
                for k in range(-B, B+1):
                    for m in range(-B, B+1):
                        window[k][m] = list(self.px[i+m, j+k])[0]
                p[i, j] = self.convolve(window)
                window[:] = 0 

        im.save('Blur/'+self.base_name)
    
