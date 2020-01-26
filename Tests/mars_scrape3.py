import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time



def foo():
    final_dictionary={}
    try:
        url = "https://twitter.com/marswxreport?lang=en"
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(url)
        time.sleep(4)
        # html = browser.html
        # soup = bs(html,'html.parser')
        # mars_weather = soup.find('span',class_='css-901oao').text
        mars_weather = browser.find_by_css('.css-901oao').find_by_partial_text('InSight sol')
        final_dictionary['Mars_weather']=mars_weather
        browser.quit()
        print(final_dictionary)
    except:
        print('wrong twitter version')
        foo()




