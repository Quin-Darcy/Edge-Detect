import math
import numpy as np
from PIL import Image

class Edge:
    def __init__(self, px, w, h, name, ws=3):
        self.px = px
        self.w = w
        self.h = h
        self.name = name
        self.base_name = name.split('/')[-1:][0]
        self.threshold = 110
        self.ws = ws

        self.set_direcs()
        self.get_edges()

    '''
    def set_kernel(self):
        self.kernel_x = np.array([[1, 0, -1], [2, 0, -1], [1, 0, -1]])
        self.kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    def convolve(self, win):
        prod_x = np.zeros((self.ws, self.ws), dtype=np.uintc)
        prod_y = np.zeros((self.ws, self.ws), dtype=np.uintc)

        for i in range(self.ws):
            for j in range(self.ws):
                prod_x = self.kernel_x[i][j] * win[i][j]
                prod_y = self.kernel_y[i][j] * win[i][j]

        prod_x = np.sum(prod_x) / (self.ws**2)
        prod_y = np.sum(prod_y) / (self.ws**2)

        return math.sqrt(prod_x**2 + prod_y**2)
    '''

    def set_direcs(self):
        B = math.floor(self.ws / 2)
        self.direcs = np.zeros((self.ws, self.ws, 2))

        for i in range(B, -B-1, -1):
            for j in range(-B, B+1):
                self.direcs[B-i][j+B] = [j, i]

    def get_gradient(self, win):
        B = math.floor(self.ws / 2)
        P = win[B][B]

        vecs = np.zeros((self.ws, self.ws, 2), dtype=np.single)

        for i in range(self.ws):
            for j in range(self.ws):
                mag = abs(float(win[i][j]) - float(P))
                vecs[i][j] = [mag*self.direcs[i][j][0], mag*self.direcs[i][j][1]]

        x = [vecs[i][j][0] for i in range(self.ws) for j in range(self.ws)]
        y = [vecs[i][j][1] for i in range(self.ws) for j in range(self.ws)]

        x = sum(x)
        y = sum(y)

        return math.sqrt(x**2 + y**2)

    def get_edges(self):
        B = math.floor(self.ws / 2)
                
        im = Image.new('RGB', (self.w, self.h), 0)
        p = im.load()

        window = np.zeros((self.ws, self.ws), dtype=np.uintc)
        for i in range(B, self.w-B):
            for j in range(B, self.h-B):
                for k in range(-B, B+1):
                    for m in range(-B, B+1):
                        window[k][m] = list(self.px[i+m, j+k])[0]
                G = self.get_gradient(window)
                if (G > self.threshold):
                    p[i, j] = (255,255,255)
                window[:] = 0 

        im.save('Edge/'+self.base_name)

    


        
