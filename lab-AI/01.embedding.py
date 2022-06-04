import tensorflow as tf

model=tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3,5),
])
#모델의 정보를 보여준다.
model.summary()