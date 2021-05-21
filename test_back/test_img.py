import pytest
import cv2
from PIL import Image, ImageChops
from application.modules.neuron.deformationImg import deformationImg


def CalcImageHash(FileName):
    image = cv2.imread(FileName)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count

@pytest.mark.parametrize('path, nameDir, file, answer', [
    ('img/', 'shakal_test/', 'bodulin.jpg', 0)
])
def test_deformationImg(path, nameDir, file, answer):
    deformationImg(path, nameDir)
    hash1 = CalcImageHash(path + nameDir + file)
    hash2 = CalcImageHash(path + 'shakal/' + file)
    assert CompareHash(hash1, hash2) == answer

# @pytest.mark.parametrize('binaryImage', 'answer', [
#     ('img/', 'shakal_test/', 'bodulin.jpg', 0)
# ])
# def test_definitionPeople():
