import tensorflow as tf

dense_model= tf.keras.models.load_model('../models/Dense.h5')
embedding_model= tf.keras.models.load_model('../models/Embedding.h5')
rnn_model= tf.keras.models.load_model('../models/RNN.h5')
softmax_model= tf.keras.models.load_model('../models/Softmax.h5')

total_models=[dense_model, embedding_model, rnn_model, softmax_model]
#모델
for model in total_models:
    predict=model.predict([[6, 7, 8, 9, 10, 11, 12, 13]])
    print(predict)