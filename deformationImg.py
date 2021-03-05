from PIL import Image
import os


def deformationImg(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            img = Image.open(root + filename)
            width = 64
            height = 64
            resized_img = img.resize((width, height), Image.ANTIALIAS)
            resized_img.save('image.png')
            print('tyt')

shakal('DataSet/Beltukov/')
