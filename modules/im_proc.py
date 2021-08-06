from modules.filters import grey
from modules.filters import enhance 
from modules.filters import blur 
from modules.filters import edge 
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
        print('Greyscaling .....')
        grey.Grey(self.px, self.W, self.H, self.base_name)
        self.im = Image.open('Images/Grey/'+self.base_name)
        self.px = self.im.load()

    def Enhance(self):
        print('Enhancing .......')
        enhance.Enhance(self.px, self.W, self.H, self.base_name)
        self.im = Image.open('Images/Enhance/'+self.base_name)
        self.px = self.im.load()

    def Blur(self, ws=3):
        print('Blurring ........')
        blur.Blur(self.px, self.W, self.H, self.base_name, ws)
        self.im = Image.open('Images/Blur/'+self.base_name)
        self.px = self.im.load()

    def Edge(self, ws=3):
        self.Grey()
        self.Blur(ws)
        print('Finding edges ...')
        edge.Edge(self.px, self.W, self.H, self.base_name)
        self.im = Image.open('Images/Edge/'+self.base_name)
        self.px = self.im.load()
        self.Enhance()
