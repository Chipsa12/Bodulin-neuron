from PIL import Image
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.saving.save import load_model
import tensorflow as tf
import numpy as np
import io

model = load_model('application/modules/neuron/definitionPeople.h5')


def resizedImg(binaryImage, size=(100, 100)):
    return Image.open(io.BytesIO(binaryImage)).resize(size, Image.ANTIALIAS)


def definitionPeople(binaryImage):
    class_names = ['Бельтюков', 'Бодулин', 'Иванов', 'Корпачев', 'Кривова',
                   'Лисина', 'Макаров', 'Пушин', 'Рябовалов', 'Тарасов', 'Титов',
                   'Фионов', 'Шудегов'
                   ]

    img = resizedImg(binaryImage)
    x = image.array_to_img(img)

    # x = x.reshape(1,10000)
    # x = 255 - x
    # x /= 255
    # print(model.__call__(np.expand_dims(x, axis=0)))

    try:
        prediction = model.predict(np.expand_dims(x, axis=0))
        prediction = np.argmax(prediction)
        print('-------------')
        print('№ class', class_names[prediction])
        print('-------------')
        return {
            'person': class_names[prediction],
            'accuracy': str(prediction)
        }
    except ValueError:
        print('-------------')
        print('Я тупой, никого не узнал!!')
        print('-------------')
        return None
