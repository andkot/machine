from pdf2image import convert_from_path
import sys
import os


def convert(file, path):
    pages = convert_from_path(file)
    counter = 1
    for page in pages:
        myfile = path + "/" + str(counter) + '.ppm'
        page.save(myfile)  
        counter+=1


if len(sys.argv)>2:
    file = sys.argv[1]
    outputDir = sys.argv[2]
    if not os.path.exists(outputDir):
            os.makedirs(outputDir)
    convert(sys.argv[1], sys.argv[2])
