import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

flag = False
while flag == False:
    try:
        final_dictionary={}
        url = "https://twitter.com/marswxreport?lang=en"
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(url)
        time.sleep(5)
        html = browser.html
        soup = bs(html,'html.parser')
        mars_weather = soup.find('p',class_='tweet-text').text

        final_dictionary['Mars_weather']=mars_weather
        browser.quit()
    
        print(final_dictionary)
        flag = True
    except:
        print('Wrong twitter version trying again')
        flag = False
        browser.quit()
