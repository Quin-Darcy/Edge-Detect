import blur
from PIL import Image

def main():
    im = Image.open('monkey.jpg')
    px = im.load()
    blur.Blur(px, im.size[0], im.size[1], 3)

if __name__ == '__main__':
    main()