import pandas as pd
import os

if not os.path.exists('../data'):
    os.mkdir('../data')

titles=['제목1', '제목2', '제목3']
data=pd.DataFrame({'title' :titles})
data.to_csv("../data/titles.csv", encoding= 'utf-8')