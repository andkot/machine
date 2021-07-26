from pdf2image import convert_from_path
from matplotlib import pyplot 
import sys
import os
import argparse


# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('-i',
                        type=str,
                        help='the path to pdf',
                        required=True)
my_parser.add_argument('-o',
                        type=str,
                        help='the path to save',
                        default='.')
my_parser.add_argument('-k',
                        choices=['save', 'show'],
                        help='не знаю что сказать, нахуй иди',
                        default='save')
my_parser.add_argument('-n',
                        type=int,
                        help='page number',
                        default=1)
# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.i
output_path = args.o
key = args.k
num = args.n

def createDir(path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    return


def saveImg(imgs, output_path):
    counter = 1
    for img in imgs:
        myfile = output_path + "/" + str(counter) + '.ppm'
        img.save(myfile)  
        counter+=1


def showImg(img):
    pyplot.imshow(img)
    pyplot.show()


def convert(input_path, output_path, key, num):
    createDir(output_path)
    pages = convert_from_path(input_path)
    if key == 'save':
        saveImg(pages, output_path)
    elif key == 'show':
        showImg(pages[num])


if __name__ == '__main__':
    convert(input_path, output_path, key, num)
