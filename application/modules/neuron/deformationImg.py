import os
import shutil

from PIL import Image


def deformationImg(path, nameDir, size=(100,100)):
    typeImg = ['jpg']
    root, dirs, files = next(os.walk(path))
    if not os.path.exists(root + nameDir):
        os.mkdir(root + nameDir)
    elif nameDir in dirs:
        shutil.rmtree(root + nameDir)
    for filename in files:
        splitFileName = filename.split('.')
        # try:
        img = Image.open(root + filename)
        if splitFileName[-1] in typeImg:
            resized_img = img.resize(size, Image.ANTIALIAS)
            resized_img.save(root + nameDir + filename)
        else:
            convertImg = img.convert('RGB')
            resized_img = convertImg.resize(size, Image.ANTIALIAS)
            resized_img.save(root + nameDir + splitFileName[0] + '.jpg')
            print('Изменили формат изображения: ', filename)
        #   except BaseException:
        #     print('Открываемый файл не является форматом изображения: ', filename)
        #     continue

def deformationAll(path, nameDir):
    root, dirs, files = next(os.walk(path))
    print(root, dirs, files)
    for dir in dirs:
        if os.path.exists(path + dir + '/'):
            root_oth, dirs_oth, files_oth = next(os.walk(path + dir + '/'))
            for dir_oth in dirs_oth:
                deformationImg(path + dir + '/' + dir_oth + '/', nameDir)
                print('Внутри папки:', dir)
        deformationImg(path + dir + '/', nameDir)
        print('Внутри папки:', dir)


# if __name__ == '__main__':
#     deformationAll('DataSet/', 'shakal/')
#     print('ok')

