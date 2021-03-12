import shutil

from PIL import Image
import os


def shakal(path):
    root, dirs, files = next(os.walk(path))
    if 'shakal' in dirs:
        shutil.rmtree(root + 'shakal')
    for filename in files:
        img = Image.open(root + filename)
        width = 64
        height = 64
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        if not os.path.exists(root + 'shakal/'):
            os.mkdir(root + 'shakal/')
        resized_img.save(root + 'shakal/' + filename)

def shakalAll(path):
    root, dirs, files = next(os.walk(path))
    print(root, dirs, files)
    for dir in dirs:
        if dir == 'Others':
            root_oth, dirs_oth, files_oth = next(os.walk(path + dir + '/'))
            for dir_oth in dirs_oth:
                shakal(path + dir + '/' + dir_oth + '/')
                print('other')
        shakal(path + dir + '/')
        print('vnutri papki')


shakalAll('DataSet/')
print('ok')
