import feedparser

# Infrastructure News RSS
rss_url = "https://news.google.com/rss/search?q=infrastructure+projects+india"

feed = feedparser.parse(rss_url)

print(f"Found {len(feed.entries)} articles\n")

for article in feed.entries[:10]:
    print("Title:", article.title)
    print("Link:", article.link)
    print("-" * 80)