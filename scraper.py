# This is a simple implementation of web scraping using BeautifulSoup
# The code below gives the articles(headlines) from India Today , dynamically....

import requests
from bs4 import BeautifulSoup

def scrape_news_from_IndiaToday(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text
        print("*"*190)
        summary = article.find('p').text
        print(title, summary)

scrape_news_from_IndiaToday('https://www.indiatoday.in/')




