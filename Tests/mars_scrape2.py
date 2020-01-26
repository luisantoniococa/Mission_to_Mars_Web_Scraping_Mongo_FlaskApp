import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


final_dictionary={}

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)


button = browser.find_by_css('.button').first.click()

featured_img = browser.find_by_css('.fancybox-image')
# html = featured_img.html
# soup = bs(html,'html.parser')
print(featured_img['src'])


# featured_img = browser.find_by_tag('img') img[src]')['src']
# featured_img_2 = featured_img.find('img')['src']
# featured_img_3 = featured_img_2['src']
featured_img_url = featured_img['src']

final_dictionary['Featured_image']=featured_img_url

browser.quit()

print(final_dictionary)
