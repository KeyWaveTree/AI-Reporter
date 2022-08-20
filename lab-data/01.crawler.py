from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# https 보안을 인증하기 위한 ssl (비공식)인증서 생성
context=ssl.create_default_context()

headers={'User-Agent': 'Mozilla/5.0'}

url='https://news.naver.com/'

#요청
request=Request(url, headers=headers)
#보내기
respense=urlopen(request, context=context)

#읽기
html=respense.read()

#파싱()
soup=BeautifulSoup(html, 'html.parser')
#find()#추출하고 싶은 부분 1가지 #all 추출하고 싶은 부분을 전부 찾고
results=soup.find_all('div', {'class', 'cjs_t'}) #{}set
#타이틀
titles=[]

#텍스트를 출력하고 싶을때
for result in results:
    print(result.text, end='')
    titles.append(result.text)

#리스트로 저장한 텍스트
print(titles)