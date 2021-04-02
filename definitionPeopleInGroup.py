from PIL import Image
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.saving.save import load_model
import numpy as np


def definitionPeople(imagePeople):

    model = load_model('definitionPeople.h5')
    class_names = ['Бельтюков', 'Бодулин', 'Иванов', 'Корпачев', 'Кривова',
                   'Лисина', 'Макаров', 'Пушин', 'Рябовалов', 'Тарасов', 'Титов',
                   'Фионов', 'Шудегов'
                   ]


    img = Image.open(imagePeople)
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
    except ValueError:
        print('-------------')
        print('Я тупой, никого не узнал!!')
        print('-------------')
