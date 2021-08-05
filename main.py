import im_proc
from PIL import Image

def main():
    I = im_proc.Convolve('Images/monkey.jpg')
    I.Blur(3)

if __name__ == '__main__':
    main()