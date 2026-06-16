import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)
import sqlite3
import feedparser
from config import DATABASE_PATH, RSS_URL

feed = feedparser.parse(RSS_URL)



conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

for article in feed.entries:

    title = article.title
    link = article.link

    cursor.execute(
        "SELECT COUNT(*) FROM news_articles WHERE url = ?",
        (link,)
    )

    exists = cursor.fetchone()[0]

    if exists == 0:

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

print(f"{len(feed.entries)} articles processed successfully.")