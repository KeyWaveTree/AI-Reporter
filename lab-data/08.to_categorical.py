#원 핫 인코딩
import tensorflow as tf

data=[0,1,2,3]
categorical_data=tf.keras.utils.to_categorical(data, num_classes=4)#0부터 num_classes미만까지 그이외 에러
print(categorical_data)