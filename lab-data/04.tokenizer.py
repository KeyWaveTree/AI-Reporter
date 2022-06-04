import tensorflow as tf
import pandas as pd

data=pd.read_csv('../data/titles.csv')
titles= data['title'].values

print(titles)
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)#fit_on_texts함수에서 정보를 집어넣으면 토큰화

word_count=len(tokenizer.word_index)+1

print(tokenizer.word_index)
print(word_count)

'''
import tensorflow as tf
import pandas as pd

data=pd.read_csv('../data/titles.csv')
titles= data['title'].values
word_index=dict()

for title in titles:
    words=title.split()
    for word in words: 
        if word not in word_index:
            word_index[word]=len(word_index)

print(word_index)            
'''
