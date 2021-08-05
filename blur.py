import math
import numpy as np
from PIL import Image

class Blur:
    def __init__(self, px, w, h, ws, var=0):
        self.px = px
        self.w = w
        self.h = h
        self.ws = ws # Window size
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

        norm_const = 1

        self.kernel = np.zeros((self.ws, self.ws))
        
        for i in range(-B, B+1):
            for j in range(-B, B+1):
                self.kernel[i+B][j+B] = norm_const * math.exp(-((j**2)/(2*var)) - ((i**2)/(2*var)))

    def convolve(self, win):
        C = math.floor(self.ws / 2)
        P = win[C][C]
        R = np.zeros((self.ws, self.ws))
        G = np.zeros((self.ws, self.ws))
        B = np.zeros((self.ws, self.ws))

        for i in range(self.ws):
            for j in range(self.ws):
                R[i][j] = self.kernel[i][j] * win[i][j][0]
                G[i][j] = self.kernel[i][j] * win[i][j][1]
                B[i][j] = self.kernel[i][j] * win[i][j][2]

        r = int((np.sum(R) / self.ws**2))
        g = int((np.sum(G) / self.ws**2))
        b = int((np.sum(B) / self.ws**2))

        return (r, g, b)

    def blur(self):
        B = math.floor(self.ws / 2)
        im = Image.new('RGB', (self.w, self.h), 0)
        p = im.load()

        window = np.zeros((self.ws, self.ws, 3), dtype=np.uintc)
        for i in range(B, self.w-B):
            for j in range(B, self.h-B):
                for k in range(-B, B+1):
                    for m in range(-B, B+1):
                        window[k][m] = list(self.px[i+m, j+k])
                p[i, j] = self.convolve(window)
                window[:] = 0 

        if (self.var == 0):
            im.save('Blur/blur_ws'+str(self.ws)+'.jpg')
        else:
            im.save('Blur/blur_ws'+str(self.ws)+'_v'+str(self.var)+'.jpg')
    
