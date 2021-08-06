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

        theta = math.atan(G_y / (G_x + 0.00001))

        return [math.sqrt(G_x**2 + G_y**2) / 1081.9, theta]

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
                if (G[0] > self.threshold):
                    p[i, j] = self.get_color(G[1])
                window[:] = 0 

        im.save('Edge/'+self.name)

    def mult(self, x,y,z):
        arr = [[math.sqrt(3)/2, 0, 1/2], [-math.sqrt(2)/4, math.sqrt(2)/2, math.sqrt(6)/4], [-math.sqrt(2)/4, -math.sqrt(2)/2, math.sqrt(6)/4]]

        vec = [x, y, z]
        newv = [0, 0, 0]

        for i in range(3):
            for j in range(3):
                newv[i] += int(vec[j] * arr[i][j])   

        return newv


    def get_color(self, t):
        arr = [0,0,0]
        k = (math.pi)/3
        a = math.sqrt(3)
        theta = (math.pi/2)-np.arccos(a/3)
        r = (127.5)*math.sqrt(3)
        c = r*a
        if (0<= t < k):
            x = c/(math.tan(t)+a)
            y = math.tan(t)*x
            z = (-(1/r)*2*x+2)*255*(math.sqrt(2)*math.sin(theta)-1/2)+127.5
            arr = self.mult(x,y,z)
        if (k<= t < 2*k):
            x = c/(2*math.tan(t))
            y = math.tan(t)*x
            z = -(1/r)*(x-r/2)*255*(1/2-math.sqrt(2)*math.sin(theta))+255*math.sqrt(2)*math.sin(theta)
            arr = self.mult(x,y,z)
        if (2*k<= t < 3*k):
            x = c/(math.tan(t)-a)
            y = math.tan(t)*x
            z = -(1/r)*(2*x+r)*255*(math.sqrt(2)*math.sin(theta)-1/2)+127.5
            arr = self.mult(x,y,z)
        if (3*k<= t < 4*k):
            x = -c/(math.tan(t)+a)
            y = math.tan(t)*x
            z = (1/r)*(2*x+2*r)*255*(1/2-math.sqrt(2)*math.sin(theta))+255*math.sqrt(2)*math.sin(theta)
            arr = self.mult(x,y,z)
        if (4*k<= t < 5*k):
            x = -c/(2*math.tan(t))
            y = math.tan(t)*x
            z = (1/r)*(x+r/2)*255*(math.sqrt(2)*math.sin(theta)-1/2)+127.5
            arr = self.mult(x,y,z)
        if (5*k <= t < 6*k):
            x = -c/(math.tan(t)-a)
            y = math.tan(t)*x
            z = (1/r)*(2*x-r)*255*(1/2-math.sqrt(2)*math.sin(theta))+255*math.sqrt(2)*math.sin(theta)
            arr = self.mult(x,y,z)

        for d in range(3):
            arr[d] = int(arr[d]*(mp)+arr[d]*(1-mp)/4)
            
        return tuple(arr)

    


        
