<!--목표(계획) 설정-->
<!--일단 쓰고나서(틀을 잡고서) 꾸미자-->
AI-Reporter
=============
데이터 분석, 딥러닝을 사용한 AI 기자 
<br/>(Using data mining and DeepLearning)
--------------------
## 프로젝트 소개
python 3.8 버전을 사용하여 프로젝트를 진행.
자연어 처리를 한 이유

<br/>

## 서론(Introduction)
### 동기(Motive)

### 일정(Schedule)

<br/>

## 본론(body) 
### 가상환경 설정(Environment Setting)
아나콘다 프롬프트를 사용하여 환경설정을 하였습니다. [Anaconda Download](https://www.anaconda.com/products/individual)
<br/> 
python 3.8 버전을 사용했습니다. 
> ***가상환경 생성 및 가상환경 동기화***
```
1. anaconda3를 다운로드 후 anaconda prompt 실행
2. conda create -n [프로젝트 이름] python=[python version]
3. activate [프로젝트 이름]
4. pip install -r requirements.txt
```

<!--I using the Anaconda prompt set up the project environment-->
<!--### 주요기능-->

### 데이터 수집 및 가공(Data collection and processing)
사용한 라이브러리:
>[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
특정 데이터를 가지고 오려면 HTML 문서에 담긴 내용을 request(요청)하여 데이터를 가져와야합니다. 기본적으로 HTML 문서전체를 추출해오기에 스크래핑 스크립트 파일에서 부과적 가공하는 코드가 많아집니다. Beautiful soup은 필요한 부분만 쉽게 뽑아서 쓰고 스크래핑에 대한 시간적 투자를 줄일 수 있기에 사용하였고 나중에는 스크래핑이아닌 크롤링으로 데이터 수집을 계획하기에 실험적으로 urllib 라이브러리를 사용하였습니다.

>ssl

>[Pandas](https://pandas.pydata.org/)

>[Tensorflow](https://www.tensorflow.org/)

#### 수집(collection)
- requset와 respense.
<br/> 기본적인 세팅을 한 뒤 urllib 라이브러리를 사용하여 request와 respense를 해줍니다.  
```
요청: request=Request(url, headers=headers)
응답: respense=urlopen(request, context=context)
```
hearder는 User-Agent 정보 context는 https 보안을 인증하기위한 정보를 가리키고 있습니다.
<br/>
- BeautifulSoup 사용.
<br/>읽어들인 HTML문서와 마크업의 문서 형태를 넣어서 파싱을 준비하고 기사 데이터인 a 태그 안에 있 는 기사 헤드라인만 파싱하여 타이틀 리스트 안에 저장하였습니다.
```
titles=[]
soup=BeautifulSoup([html이 저장되어있는 변수], 'html.parser')
headlines=soup.find_all('a', {'class', '[추출할 목록]'})

for result in headlines:
    titles.append(result.text)
 ```
 
- 데이터 저장 및 불러오기
<br/> 지정된 경로에서 파일을 생성을 한다음  pandas를 사용하여 파싱한 타이틀 변수를 데이터 프레임으로 변수화 시켰습니다. csv 파일 형태로 저장과 동시에 utf-8로 인코딩을 하면서 문자열깨짐을 방지하였습니다. 데이터 프레임을 사용한 이유는 문자 숫자 가릴거 없이 데이터를 넣어줄 수 있는 장점(변형시켜서 넣을수도 있습니다.)과 대량의 데이터를 효율적으로 처리할 수 있습니다. 
```
data=pd.DataFrame({'title' :titles})
data.to_csv("../data/titles.csv", encoding= 'utf-8')
```
<br/>

#### 가공(processing)
- 토큰화
<br/>토큰화란 말뭉치(corpus)에서 토큰(token: 문장을 문법으로 더이상 나뉠 수 없는 구조)으로 바꾸는 작업

- 배열 패딩
- 인코딩과 원 핫 인코딩

### 데이터 학습
1. 임베딩 부터 모델까지
2. 학습
3. 시각화
4. 코드 설명
5. 코드 원리
6. 예측

### 웹 애플리케이션
1. streamlit
2. 실행

### 자연어 처리
1. 단어 가방
2. 코사인 유사도

<br/>

## 결론(conclusion)<!--느낀점, 알게된점, 깨닳은 점, 새롭게 앞으로 무언가를 해결하고 싶은가-->
