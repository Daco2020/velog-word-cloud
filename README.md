# 벨로그 분석 앱
블로그의 본문을 분석하여 word cloud를 생성하는 서비스입니다.

<br>
<br>

## 사용기술
---
언어 : Python 3.8 <br>
프레임워크 : FastAPI 0.75.1 <br>
스크래핑 기술 : BeautifulSoup, konlpy <br>
워드클라우드 기술 : WordCloud, matplotlib <br>
데이터베이스 : Not used <br>

<br>
<br>


## 설치방법
---
<br>

```
poetry install
```

<br>
<br>

## 프로젝트 기간
---
22년 5월 1일 ~ 5월 31일(예정)

<br>
<br>


## 진행상황
---
- wordcloud 이미지 생성 로직 구현
- scraper 구현
- pre-commit 세팅  
    - 포멧팅 : black,flake8,isort,pyright
    - 커밋메시지 : commit-msg
- FastAPI 로컬서버 구동 확인



<br>
<br>



## 디렉토리 구조
---

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── wordcloud.py
│   ├── constant.py
│   ├── img
│   ├── main.py
│   ├── scraper.py
│   └── wordcloud.py
├── commit-msg.py
├── poetry.lock
├── pyproject.toml
├── run-server.py
├── script
│   └── git-hooks.sh
└── setup.cfg
```