import tensorflow as tf
import os

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(73, 9),
    tf.keras.layers.SimpleRNN(3),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Softmax()
])

if not os.path.exists('../models'):
    os.mkdir('../models')

model.save('../models/Softmax.h5')