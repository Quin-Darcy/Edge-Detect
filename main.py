import im_proc
from PIL import Image

def main():
    I = im_proc.Convolve('Images/gear.jpg')
    I.Edge(5)

if __name__ == '__main__':
    main()