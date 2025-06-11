# 무물보

키워드를 입력하면 해당 키워드의 최근 뉴스 제목들을 검색하고,  
가장 많이 검색된 인기 키워드까지 함께 보여주는 Flask 기반 뉴스 탐색기입니다.

---

# 배포 주소
👉 [https://moomoolbo.onrender.com](https://moomoolbo.onrender.com)

---

# 주요 기능
- Google News RSS 기반 뉴스 검색
- 키워드 입력 시 최근 7일 뉴스 제목 불러오기
- 뉴스 제목 클릭 시 해당 기사 링크로 이동
- 검색 이력을 저장하여 인기 키워드 5개 출력
- Bootstrap 5 기반 반응형 UI 적용 (모바일 대응)

---

# 사용처
 - 실시간 이슈 파악
 - 사용자 트렌드 분석
 - 연구데이터 수집 / 교육용 샘플로 이용 가능

---
# 프로젝트 구조
'''
moomoolbo/
├── app.py # 메인 Flask 애플리케이션
├── requirements.txt # 필요한 라이브러리 명세
├── Procfile # Render 배포용 실행 명령
└── templates/
└── index.html # 사용자 인터페이스 HTML
'''
---

# 기술 스택

- Python 3
- Flask
- feedparser
- Bootstrap 5 (CDN)
- Render (배포 플랫폼)

---

# 로컬 실행 방법
1. 프로젝트 클론

```bash
git clone https://github.com/Nuke1119/moomoolbo.git
cd moomoolbo
```


# 필요 패키지 설치
pip install -r requirements.txt

# 앱 실행
python app.py
→ 브라우저에서 http://localhost:5000 접속

---

# 향후 개선 예정 기능
 - 날짜 선택 기능을 통한 특정 날짜 기사 검색
 - 뉴스 요약 정보 표시 (예: 한 줄 요약)
 - 뉴스 기사 감성 분석 (긍정/부정, 주식 호재/악재 분류 등)


