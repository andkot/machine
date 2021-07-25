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

print(input_path)
print(output_path)
print(key)

def convert(input_path, output_path, key, num):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    pages = convert_from_path(input_path)
    if key == 'save':
        counter = 1
        for page in pages:
            myfile = output_path + "/" + str(counter) + '.ppm'
            page.save(myfile)  
            counter+=1
    elif key == 'show':
        pyplot.imshow(pages[num])
        pyplot.show()

convert(input_path, output_path, key, num)
