# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.preprocessing.image_dataset import image_dataset_from_directory

print(tf.__version__)

train_dataset = image_dataset_from_directory("DataSetShakal/Training",
                                            subset="training",
                                            seed=2,
                                            validation_split=0.1,
                                            batch_size=10,
                                            image_size=(100,100)
                                             )

validation_dataset = image_dataset_from_directory("DataSetShakal/Training",
                                            subset="validation",
                                            seed=2,
                                            validation_split=0.1,
                                            batch_size=10,
                                            image_size=(100,100)
                                                  )

test_dataset = image_dataset_from_directory("DataSetShakal/Test",
                                            batch_size=10,
                                            image_size=(100,100)
                                            )

class_names = train_dataset.class_names


model = Sequential()
model.add(Conv2D(16,(5,5),padding='same',
                          input_shape=(100,100,3),
                          activation='relu')
          )
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32,(5,5),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64,(5,5),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128,(5,5),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(len(class_names),activation='softmax'))


model.compile(optimizer='adam',
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

history = model.fit(train_dataset,
                    validation_data=validation_dataset,
                    epochs=8,
                    verbose=2
                    )

scores = model.evaluate(test_dataset, verbose=1)


"""Отображение результата"""
print(round(scores[1] * 100, 4))


"""Предсказала метку для каждого изображения в наборе для тестирования"""
# probability_model = Sequential([model, tf.keras.layers.Softmax()])
# predictions = probability_model.predict(test_dataset)
# print(predictions[0])


model.save('definitionPeople.h5')

"""Отображение графиков"""
# plt.plot(history.history['accuracy'],
#     label="Доля верных ответов на обучающем наборе")
# plt.plot(history.history['val_accuracy'],
#     label='Доля верных ответов на проверочном наборе')
# plt.xlabel("Эпоха обучения")
# plt.ylabel("Доля верных ответов")
# plt.legend()
# plt.show()

"""Отображение классов с картинкой"""
# plt.figure()
# plt.imshow(train_dataset[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# print('DataSetShakal/Training/Пушин/IMG_20210319_182745.jpg')
#
# def plot_value_array(i, predictions_array):
#   plt.grid(False)
#   plt.xticks(range(10))
#   plt.yticks([])
#   thisplot = plt.bar(range(10), predictions_array, color="#777777")
#   plt.ylim([0, 1])
#   predicted_label = np.argmax(predictions_array)
#
#   thisplot[predicted_label].set_color('red')
#
#
# img = 'DataSetShakal/Training/Пушин/IMG_20210319_182745.jpg'
# img = (np.expand_dims(img,0))
# predictions_single = probability_model.predict(img)
#
# plot_value_array(1, predictions_single[0], True)
# _ = plt.xticks(range(10), class_names, rotation=45)
#
# np.argmax(predictions_single[0])

