import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time




final_dictionary={}

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)


hemisphere_image_urls = []
for x in range(4):
    # print(x)
    button = browser.find_by_css('h3')[x].click()
    html = browser.html
    soup = bs(html,'html.parser')
    image = soup.find('div', class_='downloads')
    image = image.find('a')['href']
    title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({'title': title, 'img_url': image})
    browser.back()
    time.sleep(5)

final_dictionary['hemisfere_images'] = hemisphere_image_urls
browser.quit()

print(final_dictionary)