import tensorflow as tf
import pandas as pd

data=pd.read_csv('../data/titles.csv')
titles=data['title'].values

#토큰화, 문장 인코딩
tokenizer=tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

sequences=[]
max_len=0

for i in range(len(titles)):
    sequence=tokenizer.texts_to_sequences([titles[i]])[0]#
    sequences.append(sequence)
    max_len=max(max_len, len(sequence))
    # print(titles[i])
    # print(sequence)  # 문장의 인덱스 번호
    # print(max_len)  # 총 길이
 # print(sequences)

#패딩
#maxlen의 기능 가장 보내준 재료의 길이가 크거나 같아야 한다.
#0으로 값이 채워 지지만 메모리를 잡아 먹는다.
#가변 처리보다 조금 처리하기가 쉽다.
pad_sequences=tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_len)
print(pad_sequences)