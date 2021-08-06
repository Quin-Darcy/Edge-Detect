import math
from PIL import Image

class Grey:
    def __init__(self, px, w, h, name):
        self.px = px
        self.w = w
        self.h = h
        self.name = name

        self.grey()

    def convert(self, pixel):
        theta = math.acos(math.sqrt(6)/3)
        r = sum([c**2 for c in pixel])
        r = math.sqrt(r)
        C = int(r * (math.sqrt(2)/2) * math.cos(theta))
        return (C, C, C)

    def grey(self):
        im = Image.new('RGB', (self.w, self.h), 0)
        px = im.load()
        
        for i in range(self.h):
            for j in range(self.w):
                px[j, i] = self.convert(list(self.px[j, i]))

        im.save('Grey/'+self.name)