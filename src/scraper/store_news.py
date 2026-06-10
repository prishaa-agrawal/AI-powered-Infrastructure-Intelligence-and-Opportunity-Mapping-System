import sqlite3
import feedparser

rss_url = "https://news.google.com/rss/search?q=infrastructure+projects+india"

feed = feedparser.parse(rss_url)

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

for article in feed.entries:

    title = article.title
    link = article.link

    cursor.execute("""
    INSERT INTO news_articles
    (title, date, source, content, url)
    VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        "",
        "Google News",
        "",
        link
    ))

conn.commit()
conn.close()

print(f"{len(feed.entries)} articles stored successfully.")