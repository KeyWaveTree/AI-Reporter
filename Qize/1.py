from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import os
import ssl

context=ssl.create_default_context()

headers={'User-Agent': 'Mozilla/5.0'}

url='https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'

#요청
request=Request(url, headers=headers)
#보내기
respense=urlopen(request, context=context)

#읽기
html=respense.read()

soup=BeautifulSoup(html, 'html.parser')
#파싱을 해서 헤드라인 타이틀을 저장(~태그 안에, cluster_text_headline에서 nclicks(cls_sci.clsart)목록을 추출해라.
headlines=soup.find_all('a', {'class', 'cluster_text_headline nclicks(cls_sci.clsart)'})
titles=[]

for result in headlines:
    titles.append(result.text)

if not os.path.exists('../data'):
    os.mkdir('../data')


data=pd.DataFrame({'title' :titles[:10]})
data.to_csv("../data/titles.csv", encoding= 'utf-8')
