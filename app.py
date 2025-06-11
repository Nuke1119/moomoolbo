from flask import Flask, render_template, request, session
import feedparser
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def get_google_news_rss(query, days=7):
    url = f'https://news.google.com/rss/search?q={query}+when:{days}d&hl=ko&gl=KR&ceid=KR:ko'
    feed = feedparser.parse(url)
    news_items = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]
    return news_items

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword', '기술')
    news_list = get_google_news_rss(keyword)

    # 히스토리 저장 및 카운트
    if 'history' not in session:
        session['history'] = []
    if keyword:
        session['history'].append(keyword)
        session.modified = True

    # 인기 키워드 카운트
    keyword_counts = Counter(session['history'])
    hot_keywords = keyword_counts.most_common(5)  # 상위 5개

    return render_template(
        'index.html',
        news=news_list,
        selected_keyword=keyword,
        history=session['history'],
        hot_keywords=hot_keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
