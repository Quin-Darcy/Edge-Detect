from modules import im_proc 
from PIL import Image

def main():
    I = im_proc.Convolve('Images/Originals/man.jpg')
    I.Edge()

if __name__ == '__main__':
    main()