import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://news.google.com/rss/search?q=world+news&hl=en-US&gl=US&ceid=US:en"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")

        items = soup.find_all("item")
        headlines = []

        for item in items[:5]:
            title = item.title.text
            link = item.link.text
            headlines.append((title, link))

        return headlines

    except Exception as e:
        print(f"RSS fetch error: {e}")
        return []
