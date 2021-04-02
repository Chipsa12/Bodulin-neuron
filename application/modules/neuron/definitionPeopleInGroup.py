from PIL import Image
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.saving.save import load_model
import tensorflow as tf
import numpy as np
# model = load_model('definitionPeople.h5')
with tf.Session(graph=tf.Graph()) as sess:
    tf.saved_model.loader.load(sess, ["serve"], 'definitionPeople.h5')
    graph = tf.get_default_graph()
    print(graph.get_operations())
    sess.run()

def resizedImg(image, size=(100, 100)):
    return Image.open(image).resize(size, Image.ANTIALIAS)


def definitionPeople(imagePeople):
    class_names = ['Бельтюков', 'Бодулин', 'Иванов', 'Корпачев', 'Кривова',
                   'Лисина', 'Макаров', 'Пушин', 'Рябовалов', 'Тарасов', 'Титов',
                   'Фионов', 'Шудегов'
                   ]

    shakal = resizedImg(imagePeople.binary)

    img = Image.open(shakal)
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
