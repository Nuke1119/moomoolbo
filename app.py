import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)

def get_google_news_rss(query, days=7):
    # 구글 뉴스 RSS URL, days 만큼 최근 뉴스 검색
    url = f'https://news.google.com/rss/search?q={query}+when:{days}d&hl=ko&gl=KR&ceid=KR:ko'
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    return titles

@app.route('/', methods=['GET'])
def index():
    date = request.args.get('date')  # 날짜는 현재 쓰지 않고, 키워드만 받는 걸로 바꿀 수도 있음
    keyword = request.args.get('keyword', '기술')  # 기본 키워드는 '기술'

    news_list = []
    if keyword:
        news_list = get_google_news_rss(keyword)

    return render_template('index.html', news=news_list, selected_keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)
