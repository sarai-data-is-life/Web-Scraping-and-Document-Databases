from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import time

def scrape():
    browser = Browser('chrome',executable_path = 'chromedriver', headless='False')
    news_title, news_p = mars_news(browser)

    scrap_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image': featured_image(browser)
    }



    return scrap_data







def mars_news(browser):
    # Visit The NASA Mars news site
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    # browser.is_element_present_by_css('ul.item_list li.slide', wait_time=1)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    slide_elem= news_soup.select_one('ul.item_list li.slide')

    # print(slide_elem)
    # slide_elem.find('div', class_='content_title')
    news_title = slide_elem.find('div',class_='content_title').get_text()
    # news_title
    news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
    # news_p
    # print(news_title)
    # print('-' * 25)
    # print(news_p)
    return news_title, news_p

def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)  
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    img_soup = bs(html,'html.parser')
    img_url_rel = img_soup.select_one('figure.lede a img').get('src')
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url

if __name__ == '__main__':
    print(scrape())

    