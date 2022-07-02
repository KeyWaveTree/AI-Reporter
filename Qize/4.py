import tensorflow as tf
import pandas as pd


data=pd.read_csv('../data/titles.csv')
titles=data['title'].values

tokenizer=tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
word_count=len(tokenizer.word_index)+1

x=[]
y=[]

for i in range(len(titles)):
    sequence=tokenizer.texts_to_sequences(titles[i])[0]
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        x.append(sequence[j])

max_len=max(len(i) for i in x)
x=tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=max_len)
y=tf.keras.utils.to_categorical(y, num_classes=word_count)

print(x)
print(y)

# #데이터 가공 처리 변수
# sequences=[]
# categorical_data=[]
# reverse_sequence=''
# cnt=0
# max_len=0
#
# #1.데이터 가공
# #데이터 불러오기
# data=pd.read_csv('../data/titles.csv')
# titles=data['title'].values
# #토큰으로 분류함
# tokenizer=tf.keras.preprocessing.text.Tokenizer()
# tokenizer.fit_on_texts(titles)
# #print(tokenizer.word_index) 딕셔너리 형태로 문자key와 인덱스 value값으로 분류된다.
# word_count=len(tokenizer.word_index)+1
# sequence=tokenizer.texts_to_sequences([titles[0]])[0]
# #추출한 문자열의 인덱스 모음 print(sequence)
# #key와 value 바꿈
# reverse_word_index = dict(zip(tokenizer.word_index.values(),tokenizer.word_index.keys()))
#
# for i in sequence:
#     cnt += 1
#     reverse_sequence += reverse_word_index[i]
#     sequences.append(sequence[:cnt])
#     # max인수가 두개일 때 인수를 비교해 더 큰 값을 반환
#     max_len= max(max_len, len(sequence))
#
# #pad_sequences
# pad_sequences=tf.keras.preprocessing.sequence.\
#     pad_sequences(sequences, maxlen=max_len)
# print(pad_sequences)
#
# #to categorical
# for i in range(len(sequences)):
#     categorical_data.append(tf.keras.utils.\
#      to_categorical(sequences[i], num_classes=word_count))
# print(categorical_data)

