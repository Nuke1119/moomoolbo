from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

def get_google_news_rss(query, days=7):
    url = f'https://news.google.com/rss/search?q={query}+when:{days}d&hl=ko&gl=KR&ceid=KR:ko'
    feed = feedparser.parse(url)
    news_items = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]
    return news_items

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword', '기술')
    selected_date = request.args.get('date')  # 날짜 값 받기

    news_list = []
    if keyword:
        news_list = get_google_news_rss(keyword)

    return render_template(
        'index.html',
        news=news_list,
        selected_keyword=keyword,
        selected_date=selected_date
    )

if __name__ == '__main__':
    app.run(debug=True)
