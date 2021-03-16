import os
import shutil

from PIL import Image


def deformationImg(path, nameDir, size=(64, 64)):
    typeImg = ['jpg', 'png', 'jpeg']
    root, dirs, files = next(os.walk(path))
    if not os.path.exists(root + nameDir):
        os.mkdir(root + nameDir)
    elif nameDir in dirs:
        shutil.rmtree(root + nameDir)
    for filename in files:
        typeFileName = filename.split('.')[-1]
        try:
            img = Image.open(root + filename)
            if typeFileName in typeImg:
                resized_img = img.resize(size, Image.ANTIALIAS)
                resized_img.save(root + nameDir + filename)
            else:
                convertImg = img.convert('RGB')
                convertImg.save(typeFileName[0] + '.jpg')
                resized_img = convertImg.resize(size, Image.ANTIALIAS)
                resized_img.save(root + nameDir + typeFileName[0] + '.jpg')
                print('Изменили формат изображения: ', filename)
        except BaseException:
            print('Открываемый файл не является форматом изображения: ', filename)
            continue


def shakalAll(path):
    root, dirs, files = next(os.walk(path))
    print(root, dirs, files)
    for dir in dirs:
        if dir == 'Others':
            root_oth, dirs_oth, files_oth = next(os.walk(path + dir + '/'))
            for dir_oth in dirs_oth:
                deformationImg(path + dir + '/' + dir_oth + '/')
                print('other')
        deformationImg(path + dir + '/')
        print('vnutri papki')


deformationImg('DataSet/Lisina/', 'shakal/')
print('ok')
