import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time




final_dictionary = {}
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)



html = browser.html
soup = bs(html,'html.parser')
one_article = soup.find('li', class_='slide')


# for one_article in articles:
#     # print(one_article)
#     # print('-------------')


title_news = one_article.find(class_="content_title").text
paragraph = one_article.find(class_="article_teaser_body").text
# print(paragraph)
final_dictionary['latest_news'] = [title_news,paragraph]



browser.quit()

print(final_dictionary)
