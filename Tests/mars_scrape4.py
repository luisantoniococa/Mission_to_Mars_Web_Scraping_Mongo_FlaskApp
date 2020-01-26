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
articles = soup.find_all('li', class_='slide')


for one_article in articles:
    print(one_article)
    print('-------------')
    title_news = one_article.find(class_="content_title").text
    paragraph = one_article.find(class_="article_teaser_body").text
    print(paragraph)
    final_dictionary['latest_news'] = title_news,paragraph



browser.quit()


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


flag = False
while flag == False:
    try:
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



url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
table_1 = tables[0]

table_1.set_index(0, inplace=True)
table_1_html = table_1.to_html().replace('\n', '')

final_dictionary['Facts_table'] = table_1_html


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)


hemisphere_image_urls = []
for x in range(4):
    print(x)
    button = browser.find_by_css('h3')[x].click()
    html = browser.html
    soup = bs(html,'html.parser')
    image = soup.find('img', class_='wide-image')
    image = image['src']
    title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({'title': title, 'img_url': url+image})
    browser.back()
    time.sleep(5)

final_dictionary['hemisfere_images'] = hemisphere_image_urls
browser.quit()
# return final_dictionary



# print(scrape_info())
print(final_dictionary)

