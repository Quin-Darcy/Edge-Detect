import blur
import grey
import edge
from PIL import Image

class Convolve:
    def __init__(self, name):
        self.name = name
        self.base_name = name.split('/')[-1:][0]
        
        self.get_image()
        self.get_size()

    def get_image(self):
        self.im = Image.open(self.name)
        self.px = self.im.load()

    def get_size(self):
        self.W = self.im.size[0]
        self.H = self.im.size[1]

    def Grey(self):
        grey.Grey(self.px, self.W, self.H, self.base_name)

    def Blur(self, ws, v=0):
        self.Grey()
        blur.Blur(self.px, self.W, self.H, ws, 'Grey/'+self.base_name, v)

    def Edge(self):
        edge.Edge(self.px, self.w, self.h, 'Blur/'+self.base_name)
