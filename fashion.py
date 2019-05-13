# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import cv2
import sys
import os
import numpy
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

train_man_1 = []

def load_man_data():
    for filename in os.listdir(sys.argv[1]):
        img = cv2.imread(sys.argv[1] + "/" + filename)
        if img is None:
            continue

        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey = grey.tolist()
        global train_man_1
        train_man_1.append(numpy.array(grey))
    train_man_1 = numpy.array(train_man_1)

load_man_data()
exit(0)
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images/255.0
test_images = test_images/255.0
# cv2.namedWindow("Image")
# cv2.imshow("Image", train_images[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print("finish")

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=100)
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)
print(np.argmax(predictions[0]))
