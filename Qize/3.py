import tensorflow as tf
import pandas as pd
#
# sequences=[]
# reverse_sequence=''
# cnt=0
#
# data=pd.read_csv('../data/titles.csv')
# titles=data['title'].values
#
# tokenizer=tf.keras.preprocessing.text.Tokenizer()
# tokenizer.fit_on_texts(titles)
#
# sequence=tokenizer.texts_to_sequences([titles[0]])[0]
#
# reverse_word_index = dict(zip(tokenizer.word_index.values(),tokenizer.word_index.keys()))
#
# for i in sequence:
#     cnt += 1
#     reverse_sequence += reverse_word_index[i]
#     print("x=%s, y=%s" % (reverse_sequence, reverse_word_index[i+1]))
#     sequences.append(sequence[:cnt])
#     print(sequences)

data=pd.read_csv('../data/titles.csv')
titles=data['title'].values

tokenizer=tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

x=[]
y=[]

for i in range(len(titles)):
    sequence=tokenizer.texts_to_sequences(titles[i])[0]
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        y.append(sequence[j])